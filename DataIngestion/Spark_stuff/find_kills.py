#!/usr/bin/env python
# coding: utf-8
import json

import os
import math

from pyspark import SparkContext

SparkContext.setSystemProperty('spark.executor.memory', '2200m')


sc = SparkContext("spark://master:7077", "Location Finder")
sc.setLogLevel("ERROR")

print("Connected")

MAP_NAME = "Baltic_Main"
INPUT_ZONE_X = 360955
INPUT_ZONE_Y = 401233
INPUT_ZONE_RADIUS = 20718

ZONE_CENTER_OFFSET = 40000
ZONE_RADIUS_OFFSET = int(INPUT_ZONE_RADIUS / 4)


def distance_cal(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def construst_info(e):
    splitted = e.split(",")
    attacker_x = int(splitted[3])
    attacker_y = int(splitted[4])
    
    zone_x = int(splitted[9])
    zone_y = int(splitted[10])
    zone_radius = int(splitted[11])
    
    return (
        attacker_x,
        attacker_y,
        int(distance_cal(attacker_x, attacker_y, INPUT_ZONE_X, INPUT_ZONE_Y)), # Player kill location offset
        int(distance_cal(zone_x, zone_y, INPUT_ZONE_X, INPUT_ZONE_Y)), # Zone center offset
        abs(zone_radius - INPUT_ZONE_RADIUS) # zone radius offset
    )

def filter_info(e):
    return True if e[3] < ZONE_CENTER_OFFSET and e[4] < ZONE_RADIUS_OFFSET else False

whole_file_rdd = sc.textFile("hdfs://master:9000/data/{}_data.txt".format(MAP_NAME))

# start the logic from here

# split the rows and take 
splitted = whole_file_rdd.map(lambda e : construst_info(e))

filtered = splitted.filter(lambda e: filter_info(e))    


# sort by player location
final_rdd = filtered.sortBy(lambda e : e[2]).map(lambda e : (e[0], e[1])).take(5000)

final_json_string = [
    {
        "x": e[0],
        "y": e[1]
    }
    for e in final_rdd
]

print(final_json_string)

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request

# PySpark Stuff
import json
import os
import math
from pyspark import SparkContext
import time


app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return "Root"

@app.route("/weapon_ranking")
def weapon_rankning():
    # Hard coded for now because the data is not changing
    weapon_names1 = ['WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C']
    best_scopes1 = ['Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C']
    best_muzzle1 = ['Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C']
    kill_count1 = [109089, 206166, 157559, 138519, 117681, 86735, 58970, 25746, 840]
    weapon_names2 = ['WeapAK47_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapAK47_C', 'WeapAK47_C']
    best_scopes2 = ['Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C']
    best_muzzle2 = ['Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_SniperRifle_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C']
    kill_count2 = [85555, 73838, 65940, 71067, 71522, 53029, 23252, 5018, 209]
    weapon_names3 = ['WeapSCAR-L_C', 'WeapAK47_C', 'WeapAK47_C', 'WeapSKS_C', 'WeapSKS_C', 'WeapSKS_C', 'WeapAK47_C', 'WeapSCAR-L_C', 'WeapSCAR-L_C']
    kill_count3 = [70050, 66491, 40073, 35605, 33780, 23978, 11345, 3079, 124]
    best_scope3 = ['Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C']
    best_muzzle3 = ['Item_Attach_Weapon_Muzzle_FlashHider_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C']

    return jsonify(
        {
            "first": [
                {
                    "Weapon_name": name,
                    "Scope": scope,
                    "Muzzle": muzzle,
                    "Kill_Count": kill
                }
                for name, scope, muzzle, kill in zip(weapon_names1, best_scopes1, best_muzzle1, kill_count1)
            ],
            "second": [
                {
                    "Weapon_name": name,
                    "Scope": scope,
                    "Muzzle": muzzle,
                    "Kill_Count": kill
                }
                for name, scope, muzzle, kill in zip(weapon_names2, best_scopes2, best_muzzle2, kill_count2)
            ],
            "third": [
                {
                    "Weapon_name": name,
                    "Scope": scope,
                    "Muzzle": muzzle,
                    "Kill_Count": kill
                }
                for name, scope, muzzle, kill in zip(weapon_names3, best_scope3, best_muzzle3, kill_count3)
            ]
        }
    )


@app.route("/kill")
def get_kill_loc():
    raw_map_name = request.args.get('map_name')
    raw_zone_x = request.args.get('x')
    raw_zone_y = request.args.get('y')
    raw_zone_radius = request.args.get('radius')

    print("Received request with params {}, {}, {}, {}".format(raw_map_name, raw_zone_x, raw_zone_y, raw_zone_radius))
    try:
        assert int(raw_zone_x) > 0
        assert int(raw_zone_y) > 0
        assert int(raw_zone_radius) > 100
        assert len(raw_map_name) > 5
        assert raw_map_name.endswith("Main")
    except Exception:
        return jsonify({
            "status": False,
            "message": "Wrong format, check log"
        })

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

    start_time = time.time()
    sc = None

    try:
        # Now real Spark logic
        SparkContext.setSystemProperty('spark.executor.memory', '2200m')
        sc = SparkContext("spark://master:7077", "Location Finder")
        sc.setLogLevel("ERROR")

        print("Spark Connected")

        MAP_NAME = raw_map_name
        INPUT_ZONE_X = int(raw_zone_x)
        INPUT_ZONE_Y = int(raw_zone_y)
        INPUT_ZONE_RADIUS = int(raw_zone_radius)

        ZONE_CENTER_OFFSET = 40000
        ZONE_RADIUS_OFFSET = int(INPUT_ZONE_RADIUS / 4)

        whole_file_rdd = sc.textFile("hdfs://master:9000/data/{}_data.txt".format(MAP_NAME))

        # split the rows and take 
        res = whole_file_rdd \
            .map(lambda e : construst_info(e)) \
            .filter(lambda e: filter_info(e)) \
            .sortBy(lambda e : e[2]).map(lambda e : (e[0], e[1])).take(5000)

        # close spark
        sc.stop()

        return jsonify({
            "status": True,
            "data": [
                {
                    "x": e[0],
                    "y": e[1]
                }
                for e in res
            ],
            "time_spent": time.time() - start_time 
        })
    
    except Exception as ex:
        if sc is not None:
            sc.stop()

        return jsonify({
            "status": False,
            "message": str(ex)
        })


if __name__ == '__main__':
    app.run(host='master', port=12315)

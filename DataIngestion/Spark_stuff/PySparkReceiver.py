from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json

def filter(jsonEl):

    if jsonEl['_T'] != 'LogPlayerKill' and jsonEl['_T'] != 'LogPlayerMakeGroggy':
        return False

    if jsonEl['distance'] < 100:
        return False

    if 'Item_Attach_Weapon_Upper_Scope3x_C' not in jsonEl['damageCauserAdditionalInfo'] \
        and 'Item_Attach_Weapon_Upper_Scope6x_C' not in jsonEl['damageCauserAdditionalInfo']:
        return False
    

    if jsonEl['damageTypeCategory'] != "Damage_Gun":
        return False

    if jsonEl['common']['isGame'] < 1:
        return False

    return True

def reformat(jsonEl):
    output = ""

    output += jsonEl['_D'] + ','
    output += jsonEl['Map'] + ','
    output += jsonEl['killer']['name'] + ','
    output += str(jsonEl['killer']['location']['x']) + ','
    output += str(jsonEl['killer']['location']['y']) + ','
    output += str(jsonEl['victim']['location']['x']) + ','
    output += str(jsonEl['victim']['location']['y']) + ','
    output += str(jsonEl['common']['isGame']) + ','
    output += jsonEl['damageCauserName'] + ','
    scope = 'None'
    for a in jsonEl['damageCauserAdditionalInfo']:
        if "Scope" in a:
            scope = a
            break
    output += scope + ","
    muzzle = 'None'
    for a in jsonEl['damageCauserAdditionalInfo']:
        if "Muzzle" in a:
            muzzle = a
            break
    output += muzzle + ","
    return output

import ast

def convertToJson(e):
    
    r = e.replace("\"", "\'")
    # print(r)
    stringVersion = ast.literal_eval(r)
    return stringVersion


SparkContext.setSystemProperty('spark.executor.memory', '10g')
# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[3]", "NetworkWordCount")

sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 15)

lines = ssc.socketTextStream("localhost", 9999)


# lines.pprint()
lines = lines.flatMap(lambda line: line.split(" "))
lines = lines.map(convertToJson)
# lines.pprint()
playerKillEvents = lines.filter(filter)
playerKillEvents = playerKillEvents.map(reformat)


print("")
playerKillEvents.pprint()
playerKillEvents.saveAsTextFiles("Results.txt")

ssc.start()             # Start the computation
ssc.awaitTermination()  #

SparkContext.stop(sc)

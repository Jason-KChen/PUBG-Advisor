import sys
import math
import time



class KillLocationFinder:

    def __init__(self, mapPath, x, y, searchRadius):
        self.mapPath = mapPath
        self.x = int(x)
        self.y = int(y)
        self.searchRadius = int(searchRadius)
        self.ZONE_CENTER_OFFSET = 40000
        self.ZONE_RADIUS_OFFSET = int(self.searchRadius / 4)

    def distance_cal(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)    

    def filter_info(self, e):
        return True if e[3] < self.ZONE_CENTER_OFFSET and e[4] < self.ZONE_RADIUS_OFFSET else False

    def findKills(self):
        killLocations = []
        lenOfKL = 0
        with open(self.mapPath, "r") as file:
            start = time.time()
            for index, line in enumerate(file):
                if index % 1000000 == 0:
                    print(f"index is currently at {index}. Total time elapsed is {time.time() - start}")

                splitted = line.split(",")
                attacker_x = int(splitted[3])
                attacker_y = int(splitted[4])
                
                zone_x = int(splitted[9])
                zone_y = int(splitted[10])
                zone_radius = int(splitted[11])

                el = (
                    attacker_x,
                    attacker_y,
                    int(self.distance_cal(attacker_x, attacker_y, self.x, self.y)), # Player kill location offset
                    int(self.distance_cal(zone_x, zone_y, self.x, self.y)), # Zone center offset
                    abs(zone_radius - self.searchRadius) # zone radius offset
                )
                killLocations.append(el)
                
                #if self.filter_info(el):
                #    if lenOfKL > 5000:
                #        killLocations.remove(min(killLocations, key=lambda x: x[2]))
                #        lenOfKL -= 1
                #    # print("Adding el")
                #    killLocations.append(
                #        el
                #    )
                #    lenOfKL += 1
        print(len(killLocations))
        killLocations = [
            e for e in killLocations if e[3] < self.ZONE_CENTER_OFFSET and e[4] < self.ZONE_RADIUS_OFFSET
        ]
        killLocations.sort(key=lambda e: e[2])
        

        print(f"total time is {time.time() - start}")
        return map(lambda x: (x[0], x[1]), killLocations)


if __name__== "__main__":
    if len(sys.argv) != 5:
        print("Proper usage: python LocationAdvisingScript.py <path to map> <x> <y> <search radius>")
        exit()
    finder = KillLocationFinder(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    finder.findKills()

import json
import requests
import os
import sys

from time import sleep
from multiprocessing import Pool
from random import randrange
from dotenv import load_dotenv
load_dotenv()

ALL_SCOPES = set([
    "Item_Attach_Weapon_Upper_ACOG_01_C",
    "Item_Attach_Weapon_Upper_Aimpoint_C",
    "Item_Attach_Weapon_Upper_CQBSS_C",
    "Item_Attach_Weapon_Upper_DotSight_01_C",
    "Item_Attach_Weapon_Upper_Holosight_C",
    "Item_Attach_Weapon_Upper_PM2_01_C",
    "Item_Attach_Weapon_Upper_Scope3x_C",
    "Item_Attach_Weapon_Upper_Scope6x_C"
])

ALL_MUZZLES = set([
    "Item_Attach_Weapon_Muzzle_Choke_C",
    "Item_Attach_Weapon_Muzzle_Compensator_Large_C",
    "Item_Attach_Weapon_Muzzle_Compensator_Medium_C",
    "Item_Attach_Weapon_Muzzle_Compensator_SniperRifle_C",
    "Item_Attach_Weapon_Muzzle_Duckbill_C",
    "Item_Attach_Weapon_Muzzle_FlashHider_Large_C",
    "Item_Attach_Weapon_Muzzle_FlashHider_Medium_C",
    "Item_Attach_Weapon_Muzzle_FlashHider_SniperRifle_C",
    "Item_Attach_Weapon_Muzzle_Suppressor_Large_C",
    "Item_Attach_Weapon_Muzzle_Suppressor_Medium_C",
    "Item_Attach_Weapon_Muzzle_Suppressor_Small_C",
    "Item_Attach_Weapon_Muzzle_Suppressor_SniperRifle_C"
])

def rand_sleep():
    # anti DDoS
    sleep(randrange(1, 2))

def get_partition_content(partition_number):
    res = []

    with open(f"data_partitions/filtered_match_ids_partition_{partition_number}.txt", "r") as f:
        res = [x.strip() for x in f.readlines()]

    print(f"Read {len(res)} matches")

    return res


def split_match_meta(match_meta_list, partitions):
    res = []
    total_count = len(match_meta_list)
    num_remaining = total_count

    limit = total_count // partitions
    start_idx = 0

    while start_idx < total_count:
        curr_seg_count = min(num_remaining, limit)
        num_remaining -= curr_seg_count

        res.append(
            (match_meta_list[start_idx: start_idx + curr_seg_count],)
        )
        
        start_idx += curr_seg_count

    return res


def parallel_match_parsing(match_list):
    def get_scope(attachment_list):
        for e in attachment_list:
            if e in ALL_SCOPES:
                return e

        return "None"

    def get_muzzle(attachment_list):
        for e in attachment_list:
            if e in ALL_MUZZLES:
                return e

        return "None"

    curr_pid = os.getpid()
    API_HEADERS = {
        "Accept": "application/vnd.api+json"
    }

    kill_details = []
    curr_count = 0
    fetch_fail_count = 0
    parse_fail_count = 0
    good_count = 0

    for match_info in match_list:
        # if curr_count == 20:
        #     break

        if curr_count % 150 == 0:
            print(f"Process {curr_pid}: Currently on {curr_count} out of {len(match_list)} matches with {fetch_fail_count} fetch and {parse_fail_count} parse errors")

        telemetric_url, time_string, map_name = match_info.split(",")
        res = None
        
        # Fetching
        try:
            res = requests.get(telemetric_url, headers=API_HEADERS)
            assert res.status_code == 200

        except Exception as e:
            fetch_fail_count += 1
            curr_count += 1
            print(f"Network failure in process {curr_pid}")

            # network failure, sleep longer
            sleep(10)
            continue

        # Parsing
        try:
            events = json.loads(res.text)
            for e in events:
                # applying filter as stated in issue 4
                if (e["_T"] == "LogPlayerKill" or e["_T"] == "LogPlayerMakeGroggy") and \
                    e["damageTypeCategory"] == "Damage_Gun" and \
                    e["common"]["isGame"] >= 1 and \
                    e["distance"] > 100:

                    attacker_name = "killer" if e["_T"] == "LogPlayerKill" else "attacker"

                    kill_details.append(
                        "{},{},{},{},{},{},{},{},{},{},{}".format(
                            time_string,
                            map_name,
                            e[attacker_name]["name"],
                            int(e[attacker_name]["location"]["x"]),
                            int(e[attacker_name]["location"]["y"]),
                            int(e["victim"]["location"]["x"]),
                            int(e["victim"]["location"]["y"]),
                            e["common"]["isGame"],
                            e["damageCauserName"],
                            get_scope(e["damageCauserAdditionalInfo"]),
                            get_muzzle(e["damageCauserAdditionalInfo"])
                        )
                    )

                    good_count += 1
            
        except KeyError as error:
            print(error)
            parse_fail_count += 1
            curr_count += 1

            rand_sleep()
            continue

        rand_sleep()
        curr_count += 1

    print(f"Finished with {curr_count} matches analyzed and found {good_count} kills")
    # print(kill_details)

    return kill_details


def parse_match_data(partition_number, parallel = 3):
    all_match_meta = get_partition_content(partition_number)

    print(f"Running on parition {partition_number} and parallel factor {parallel}")
    # print(len(split_match_meta(all_match_meta, parallel)))
    with Pool(parallel) as p:
        results = p.starmap(
            parallel_match_parsing,
            split_match_meta(all_match_meta, parallel)
        )

        count = 0
        if os.getenv("mode") == "dev":
            # write to disk
            with open(f'data_partitions/parsed_data_partition_{partition_number}.txt', 'w+') as f:
                for res in results:
                    for e in res:
                        f.write("{}\n".format(e))

                        count += 1

        else:
            # Write to Mongo, TODO
            pass

        print(f"Finished with {count} kills")


if __name__ == "__main__":
    # run this file like python parse_match_data.py 3 5
    partition_number = sys.argv[1]

    if len(sys.argv) == 3:
        parse_match_data(partition_number, int(sys.argv[2]))
    else:
        parse_match_data(partition_number)


import json
import requests
import os
import sys

from multiprocessing import Pool
from time import sleep
from random import randrange
from dotenv import load_dotenv
load_dotenv()


# Filter matches on mode
# only allow the following
# gameMode: duo, duo-fpp, solo, solo-fpp, squad, squad-fpp
# matchType: official
# isCustomMatch: false

# we extract the following
# telemetricObjURL, createdAt, mapName

def rand_sleep():
    # anti DDoS
    sleep(randrange(1, 3))


def get_all_matches(file_name):
    all_match_ids = []

    with open(file_name, 'r') as f:
        all_match_ids = [x.strip() for x in f.readlines()] 

    print(f"Read {len(all_match_ids)} players")


def parallel_discover_matches_and_filter(matches):
    BASE_URL = "https://api.pubg.com/shards/steam/matches/{}"
    mode_filter = set("duo", "duo-fpp", "solo", "solo-fpp", "squad", "squad-fpp")
    MATCH_TYPE = "official"
    IS_CUSTOM_MATCH = False

    curr_pid = os.getpid()
    match_details = []
    curr_count = 0
    fetch_fail_count = 0
    parse_fail_count = 0

    for match in matches:
        if curr_count == 20:
            break

        if curr_count % 1000 == 0:
            print(f"Process {curr_pid}:Currently on {curr_count} out of {len(match)} players")

        match_details_url = BASE_URL.format(match)

        # request data from api and check if the connect is successfully
        response = requests.get(match_details_url)

        if response.status_code != 200:
            print(f"Failed to fetch stats for {matches}")
            fetch_fail_count += 1

            rand_sleep()
            continue

        match_stat = json.loads(response.text)

        try:
            # lazy way to check everything exists and matches expected
            assert match_stat["data"]["attributes"]["isCustomMatch"] == IS_CUSTOM_MATCH
            assert match_stat["data"]["attributes"]["matchType"] == MATCH_TYPE
            assert match_stat["data"]["attributes"]["gameMode"] in mode_filter
            
            # need them to exist
            match_stat["data"]["attributes"]["createdAt"]
            match_stat["data"]["attributes"]["mapName"]
            match_stat["data"]["includes"]
        except Exception as e:
            parse_fail_count += 1

            rand_sleep()
            continue

        # get the telemetric ID
        all_includes = match_stat["data"]["includes"]
        for e in all_includes:
            if e["type"] == "asset":
                # Found the right location
                match_details.append(
                    (
                        e["attributes"]["URL"],
                        match_stat["data"]["attributes"]["createdAt"],
                        match_stat["data"]["attributes"]["mapName"]
                    )
                )

                break

        # Done, wait and move forward
        rand_sleep()


def discover_matches_and_filter(parition_file_name):
    match_id = get_all_matches(partition_file_name)
    


if __name__ == "__main__":
    ## run this script with the file name of the match id partition
    partition_file_name = sys.argv[1]

    # run the script
    discover_matches_and_filter(partition_file_name)
        












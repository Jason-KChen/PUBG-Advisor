
import json
import requests
import os

from multiprocessing import Pool
from time import sleep
from dotenv import load_dotenv
load_dotenv()

from util import writeToMongo


BASE_URL = "https://api.pubg.com/shards/steam/"

def gen_API_headers(key):
    return {
        "Authorization": "Bearer " + key,
        "Accept": "application/vnd.api+json"
    }


def get_players():
    player_names = []

    with open('player_names.txt', 'r') as f:
        player_names = [x.strip() for x in f.readlines()] 

    print(f"Read {len(player_names)} players")

    return player_names

def parrallelize_fetching(player_names, api_header):
    curr_pid = os.getpid()
    match_id_collected = set()
    curr_count = 0

    for player_name in player_names:
        # if curr_count == 20:
        #     break

        if curr_count % 10 == 0:
            print(f"Process {curr_pid}:Currently on {curr_count} out of {len(player_names)} players")

        player_stats_url = "{}players?filter[playerNames]={}".format(BASE_URL, player_name)

        # request data from api and check if the connect is successfully
        response = requests.get(player_stats_url, headers=api_header)

        if response.status_code != 200:
            print(f"Failed to fetch stats for {player_name}")
            sleep(6.2)
            continue

        player_stat = json.loads(response.text)

        try:
            player_stat['data'][0]['relationships']['matches']['data']
        except Exception as e:
            print(f"Invalid data received for {player_name}")
            sleep(6.2)
            continue

        match_obj_list = player_stat['data'][0]['relationships']['matches']['data']
        for match_obj in match_obj_list:
            match_id_collected.add(match_obj['id'])

        sleep(6.2)
        curr_count += 1

    return list(match_id_collected)


def fetch_match_ids():
    player_names = get_players()
    final_match_ids = set()
    total_num_names = len(player_names)

    print(f"Total number of players: {total_num_names}")

    with Pool(4) as p:
        results = p.starmap(
            parrallelize_fetching,
            [
                (player_names[:total_num_names // 4], gen_API_headers(os.getenv("key0"))),
                (player_names[total_num_names // 4 + 1: total_num_names // 4 * 2], gen_API_headers(os.getenv("key1"))),
                (player_names[total_num_names // 4 * 2 + 1: total_num_names // 4 * 3], gen_API_headers(os.getenv("key2"))),
                (player_names[total_num_names // 4 * 3 + 1:], gen_API_headers(os.getenv("key3"))),
            ]
        )

        for res in results:
            for e in res:
                final_match_ids.add(e)

    print(f"Finished, we got {len(final_match_ids)} matches")

    if os.getenv("mode") == "dev":
        # write to disk
        with open('match_ids.txt', 'w+') as f:
            for match_id in list(final_match_ids):
                f.write("{}\n".format(match_id))
    else:
        # Write to Mongo, TODO
        writeToMongo(final_match_ids)
        pass
        

if __name__ == "__main__":
    fetch_match_ids()
    exit()

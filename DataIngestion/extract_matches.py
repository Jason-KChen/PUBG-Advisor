
import json
import requests
import os
from time import sleep

from dotenv import load_dotenv
load_dotenv()


BASE_URL = "https://api.pubg.com/shards/steam/"
API_HEADERS = {
    "Authorization": "Bearer " + os.getenv("key"),
    "Accept": "application/vnd.api+json"
}

def get_players():
    player_names = []

    with open('player_names.txt', 'r') as f:
        player_names = [x.strip() for x in f.readlines()] 

    print(f"Read {len(player_names)} players")

    return player_names


def fetch_match_ids():
    player_names = get_players()
    count = 0

    match_ids = set()

    for player_name in player_names:
        if count == 20:
            break

        if count % 10 == 0:
            print(f"Currently on {count} out of {len(player_names)} players")

        player_stats_url = "{}players?filter[playerNames]={}".format(BASE_URL, player_name)
        print(player_stats_url)

        # request data from api and check if the connect is successfully
        response = requests.get(player_stats_url, headers = API_HEADERS)

        if response.status_code != 200:
            print(f"Failed to fetch stats for {player_name}")

        player_stat = json.loads(response.text)

        try:
            player_stat['data'][0]['relationships']['matches']['data']
        except Exception as e:
            print(f"Invalid data received for {player_name}")
            # print(player_stat)
            sleep(6.3)
            continue

        match_obj_list = player_stat['data'][0]['relationships']['matches']['data']
        for match_obj in match_obj_list:
            match_id = match_obj['id']
            match_ids.add(match_id)

            # TODO
            # save to DB
            # if not exists, check match type is official 
            # send to spark

        sleep(6.3)
        count += 1

    print(match_ids)
        

if __name__ == "__main__":
    fetch_match_ids()
    exit()

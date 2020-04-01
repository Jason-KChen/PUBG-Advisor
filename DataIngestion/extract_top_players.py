import json
import requests
import os
import time

from dotenv import load_dotenv
load_dotenv()


BASE_URL = "https://api.pubg.com/shards/steam/"
API_HEADERS = {
    "Authorization": "Bearer " + os.getenv("key"),
    "Accept": "application/vnd.api+json"
}

def extract_top_players():
    # from leaderboards
    leaderboard_url = BASE_URL + "leaderboards/division.bro.official.pc-2018-06/"
    modes = ['solo', 'duo', 'squad'] #, 'solo-fpp', 'duo-fpp', 'squad-fpp']

    top_player_ids = set()

    for mode in modes:
        count = len(top_player_ids)
        leaderboard_url_with_Mode = "{}{}?page[number]=0".format(leaderboard_url, mode)

        # request data from api and check if the connect is successfully
        rleader = requests.get(leaderboard_url_with_Mode, headers=API_HEADERS)
        if rleader.status_code == 200:
            print("Processing {}".format(mode))
        else:
            print("Skipping {} because {}".format(mode, rleader.status_code))

            continue

        season_stat = json.loads(rleader.text)

        # we extract the player id list from the season object
        # we need the names instead of the account.accountID.
        # Easier for comparison later on
        player_objects = season_stat["included"]

        for player_object in player_objects:
            top_player_ids.add(player_object["attributes"]["name"])

        print("Added {} players in mode {}".format(len(top_player_ids) - count, mode))

    print("Total {} unique players".format(len(top_player_ids)))

    # We will be multiprocessing match lookup, so write to disk is an easier format to split loads
    with open('player_names.txt', 'w+') as f:
        for player_name in list(top_player_ids):
            f.write("{}\n".format(player_name))


if __name__ == "__main__":
    extract_top_players()

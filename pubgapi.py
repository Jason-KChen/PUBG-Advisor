import requests
import json
import pandas as pd
import time
#from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

url = "https://api.pubg.com/shards/steam/"
 
load_dotenv(find_dotenv())

headers = {
  "Authorization": "Bearer " + os.getenv("key"),
  "Accept": "application/vnd.api+json"
}





#leaderboards
leaderboard_url = url + "leaderboards/division.bro.official.pc-2018-06/"
topPlayerIDList = []

modes = ['solo', 'duo', 'squad', 'solo-fpp', 'duo-fpp', 'squad-fpp']
for mode in modes:
	leaderboard_urlwMode = leaderboard_url + "{}?page[number]=0".format(mode)
	#print(leaderboard_urlwMode)
	# request data from api and check if the connect is successfully
	rleader = requests.get(leaderboard_urlwMode, headers = headers)
	if rleader.status_code == 200:
		print("Successfully Connected!!!", mode)
	else:
	  print('Failed to Connect!!!', mode, rleader.status_code)
	season_stat = json.loads(rleader.text)
	# we extract the player id list from the season object
	leaderID_list = season_stat['data']['relationships']['players']['data']

	for leaderID in leaderID_list:
		topPlayerIDList.append(leaderID['id']) if leaderID['id'] not in topPlayerIDList else topPlayerIDList

# df = pd.DataFrame({'plaerID':topPlayerIDList}) 
# df.to_csv('topPlayerIDList.csv', index=False, encoding='utf-8')
time.sleep(40)




#player
matchIDList = []
for topPlayerID in topPlayerIDList:
	time.sleep(6.2)
	player_stats_url = url + "players/{}".format(topPlayerID)

	# request data from api and check if the connect is successfully
	rplayer = requests.get(player_stats_url, headers = headers)
	# if rplayer.status_code == 200:
	# 	print("Successfully Connected!!!")
	# else:
	#   print("Failed to Connect!!!", rplayer.status_code)
	if rplayer.status_code != 200:
		print("Failed to Connect!!!", rplayer.status_code)
	player_stat = json.loads(rplayer.text)

	#print(json.dumps(player_stat, sort_keys=False, indent=4))

	# we extract the match id list from the player object
	match_id_list = player_stat['data']['relationships']['matches']['data']
	for match_id in match_id_list:
		matchIDList.append(match_id['id']) if match_id['id'] not in matchIDList else matchIDList
	
df = pd.DataFrame({'matchID':matchIDList}) 
df.to_csv('matchID.csv', index=False, encoding='utf-8')



# #match
# # print info of each match
# def print_match_stats(match_stat):
#   match_id = match_stat['data']['id']
#   match_attributes = match_stat['data']['attributes']
#   print("match_id: ", match_id)
#   print(json.dumps(match_attributes, sort_keys=False, indent=4))
#   return

# # print the performance stats of the searched player in each match
# def print_participant_performance(player_name, match_stat):
#   match_included = match_stat['included']
#   for i in match_included:
#     if (i['type'] == 'participant' and i['attributes']['stats']['name'] == player_name):
#       sub = i['attributes']['stats']
#       print(json.dumps(sub, sort_keys=False, indent=4))
#   return

	# for match in match_id_list:
	#   match_id = match['id']
	#   match_url = url + "matches/{}".format(match_id)
	#   match_r = requests.get(match_url, headers = headers)
	#   if match_r.status_code != 200:
	#     print("Failed to Connect!!!")
	#   match_stat = json.loads(match_r.text)
  
#   # Since there is too many data in the match object, we only show two things here:
#   # match info and one participant performance
#   print("****************************************************\n")
#   print_match_stats(match_stat)
#   print_participant_performance(player_name, match_stat)



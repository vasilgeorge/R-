import json
import requests
from pprint import pprint
from venue_tips import get_tips
from nltk.tokenize import word_tokenize
import nltk

url = 'https://api.foursquare.com/v2/venues/45697387f964a520e53d1fe3/menu'

params = dict(
  client_id='PONVIEDXX32AFZ51UON4UW2GXRKAFUJW3O1LUWOT2UMHDTSH',
  client_secret='ZDAMCXIOKYKNF2WFN05QI3HNZTATHTFL1BGFN3XILEGLYNB4',
  v='20170801',															# Date
  VENUE_ID = "45697387f964a520e53d1fe3"

)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

#print(data["response"]["menu"]["menus"]["items"][0]["entries"]["items"][0]["name"]) 	# General  catergoric dishes  (e.g. salads, soups, main_dishes..)
tips_tok = []
tips = get_tips()
tips.append("Bonquerones Salad was great!")	
#tips_tok.append(["Bonquerones Salada was great!"])	
#print(tips)	# Get tips for that restaurant
for i in range(len(tips)):
	tips_tok.append(word_tokenize(tips[i])) # It is a list of lists
											# This is the correct way to refer to the elements of tips_tok: print(tips_tok[i][j])	

tips_token = []											
for i in range(len(tips_tok)):
	tips_token = tips_token + tips_tok[i]
#print (tips_token)	

menu = []

"""Print all the dishes of a specific category"""
for j in range (int(data["response"]["menu"]["menus"]["items"][0]["entries"]["count"])):
	#print(data["response"]["menu"]["menus"]["items"][0]["entries"]["items"][j]["name"])
	for i in range(int(data["response"]["menu"]["menus"]["items"][0]["entries"]["items"][0]["entries"]["count"])):
		#print(data["response"]["menu"]["menus"]["items"][0]["entries"]["items"][j]["entries"]["items"][i]["name"]) # Exact dish over a category
		menu.append(data["response"]["menu"]["menus"]["items"][0]["entries"]["items"][j]["entries"]["items"][i]["name"])
	#print("\n")	

menu_tok = []
for i in range(len(menu)):
	menu_tok.append(word_tokenize(menu[i]))	

# menu_token = []											
# for i in range(len(menu_tok)):
# 	menu_token = menu_token + menu_tok[i]
#print (menu_tok[0][0],menu_tok[0][1])	

#print("\n")
#print(tips_tok[0])
#print(menu_tok[0][0])

""" Some names of dishes consist of more than one word, so I need to be careful when comparing tips from users with dish names."""
similar = []
similarity = 0 # Similarity should be checked so that common words such as "a" do not count.
"""Totally naive implementation - Probably I will need to use some dictionaries or stuff like this - A good idea would be to create a vocabulary for each venue and correspond words to integers.
Basically all venues will have the samve vocabulary, but in each venue we will add some extra words that correspond to the menu words."""


"""Should use nltk.edit_distance to check how different some words are so as to consider that the user might have made a spelling error and we should forgive that."""
for i in range(len(tips_token)):
	for j in range(len(menu_tok)):
		for k in range(len(menu_tok[j])):
			if nltk.edit_distance(tips_token[i],menu_tok[j][k]) <2:
				if k+1 < len(menu_tok[j]):
					if nltk.edit_distance(tips_token[i+1],menu_tok[j][k+1])<2: # Needs another control : maybe should check more than 2 consecutive words. Maybe 3 or so.
						similarity += 1
						similar.append(menu_tok[j][k]+ " "+ menu_tok[j][k+1])
print(similarity,"\n")
print(similar)	

#	Sentiment analysis following ... I should analyze each tip of a user to categorize it into positive, negative or neutral iff a word related to a menu dish is included in this sentence.
























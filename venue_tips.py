import json
import requests
from pprint import pprint
import nltk
import numpy as np

def get_tips():
	url = 'https://api.foursquare.com/v2/venues/45697387f964a520e53d1fe3/tips'

	params = dict(
	  client_id='PONVIEDXX32AFZ51UON4UW2GXRKAFUJW3O1LUWOT2UMHDTSH',
	  client_secret='ZDAMCXIOKYKNF2WFN05QI3HNZTATHTFL1BGFN3XILEGLYNB4',
	  v='20170801',															# Date
	  VENUE_ID = "45697387f964a520e53d1fe3",
	  sort = "recent",
	  limit = "20",
	  offset = "20"

	)
	tips = []
	resp = requests.get(url=url, params=params)
	data = json.loads(resp.text)
	#print(data)
	for i in range(20):
		tips.append(data["response"]["tips"]["items"][i]["text"])
	#print (len(tips))
	return tips




get_tips()	
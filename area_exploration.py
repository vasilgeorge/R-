import json
import requests
from pprint import pprint

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='PONVIEDXX32AFZ51UON4UW2GXRKAFUJW3O1LUWOT2UMHDTSH',
  client_secret='ZDAMCXIOKYKNF2WFN05QI3HNZTATHTFL1BGFN3XILEGLYNB4',
  v='20170897',															# Date
  ll='40.722547, -73.998834',											# Co-ordinates of a place
  query='food',															
  limit=2	
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
#print(data)
print(data["response"]["groups"][0]["items"][0]["venue"]["id"])
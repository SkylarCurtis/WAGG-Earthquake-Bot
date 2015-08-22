import requests, tweepy
from english import English

url = 'http://earthquake.usgs.gov/earthquakes/feed' \
		'/v1.0/summary/significant_hour.geojson'

r = requests.get(url)
if r.status_code == 200:
	print r.json()
else:
	print "Error: Status code {}".format(r.status_code)

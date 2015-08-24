import requests, tweepy
from english import English

url = 'http://earthquake.usgs.gov/earthquakes/feed' \
		'/v1.0/summary/significant_hour.geojson'

test_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson'

r = requests.get(test)
if r.status_code == 200:
	if len(r.json()['features']) > 0:
		s = English(r.json())
		print s.sentence()
else:
	print "Error: Status code {}".format(r.status_code)

import requests, random
from english import English
from twitter import Twitter

url = 'http://earthquake.usgs.gov/earthquakes/feed' \
		'/v1.0/summary/significant_hour.geojson'

test_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson'

r = requests.get(test_url)
if r.status_code == 200:
	if len(r.json()['features']) > 0:
		s = English(r.json())
		t = Twitter()
		t.tweet("{} {}".format(s.sentence(), random.randint(0, 1000)))
else:
	print "Error: Status code {}".format(r.status_code)

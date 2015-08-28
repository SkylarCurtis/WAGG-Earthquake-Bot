WAGG-Earthquake-Bot
===================

A Twitter bot that tweets when significant earthquakes occur.

We'll be using [USGS's API](http://earthquake.usgs.gov/fdsnws/event/1/), specifically `significant_hour`, for the latest important earthquake reports:

```
http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson
```

To do
-----

- [ ] Add support to give English class an array of earthquake events
and have it parse all objects
- [ ] Remove methods to return values and instead use `@property` for cleaner syntax

Testing
-------

```bash
git clone git@github.com:WAGGNews/WAGG-Earthquake-Bot
cd WAGG-Earthquake-Bot
pip install -r requirements.txt
python WAGG-Earthquake-Bot/main.py
```

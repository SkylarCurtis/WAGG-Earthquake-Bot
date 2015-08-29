"""
Parses input into native, aesthetically pleasing English
Example of tweet style at twitter.com/WAGGNews/status/633736182782758913
"""

import datetime

class English():
    def __init__(self, input):
        self.input = input
        self.properties = self.input['features'][0]['properties']

    def raw(self): return self.input
    def place(self): return self.properties['place']
    def magnitude(self): return self.properties['mag']
    def url(self): return self.properties['url']

    def time(self):
        timestamp = self.properties['time']
        value = datetime.datetime.fromtimestamp(timestamp/1000)
        return value.strftime("%H:%M on %B %d, %Y")

    def sentence(self):
        values = {
            "magnitude":self.magnitude(), "place":self.place(),
            "time":self.time(), "url":self.url() }
        return "Magnitude {magnitude} earthquake hits {place} at {time} UTC " \
        "– @USGS {url}".format(**values)

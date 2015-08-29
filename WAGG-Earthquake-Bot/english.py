"""
Parses input into native, aesthetically pleasing English
Example of tweet style at twitter.com/WAGGNews/status/633736182782758913
"""

import datetime

# Braerules
# Numbers < 10 to be spelled out
# Distance measurement spelled out
class English():
    def __init__(self, input):
        self.input = input
        self.properties = self.input['features'][0]['properties']

    def raw(self): return self.input
    def magnitude(self): return self.properties['mag']
    def url(self): return self.properties['url']
    def place(self): return self.properties['place']

    def time(self):
        timestamp = self.properties['time']
        value = datetime.datetime.fromtimestamp(timestamp/1000)
        return value.strftime("%H:%M on %B %d, %Y")

    def sentence(self):
        values = {
            "magnitude":self.magnitude(), "place":self.place(),
            "time":self.time(), "url":self.url() }
        return "Magnitude {magnitude} earthquake hits {place} at {time} UTC " \
        "- {url}".format(**values)

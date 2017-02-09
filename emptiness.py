#!/bin/python
from html.parser import HTMLParser
import requests

class courseParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

if __name__ == '__main__':
	parser = courseParser

	# Get HTML file
	htmlRequest = requests.get("http://upnet.up.ac.za/tt/hatfield_timetable.html")
	print(htmlRequest.content)

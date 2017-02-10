#!/bin/python

import argparse

import requests
import timetable

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument("-d", "--day", default='', required=True, help="Day to check the timetable on. eg: Thursday")
	parser.add_argument("-t", "--time", default='', required=True, help="The time the block must be empty (HH:MM (24h))")

	args = parser.parse_args()

	htmlRequest = requests.get("http://upnet.up.ac.za/tt/hatfield_timetable.html")

	timeTableObject = timetable.parseHTMLFile(htmlRequest.text)

	# Method 1 ; Elimination
	venueList = timetable.getVenueList(timeTableObject)

	filteredTimetable = timetable.getFilteredTimetable(args.day, args.time, timeTableObject, venueList)

	#for el in filteredTimetable:
	#	print(el.venue)

	empty = timetable.getEmptyVenues(filteredTimetable, venueList)

	for el in empty:
		print(el)

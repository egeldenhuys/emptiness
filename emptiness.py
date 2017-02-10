#!/bin/python

__version__ = 'v1.0.0'

import argparse
import requests
import timetable
import datetime
import time

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', '--day', default='', required=False, help="Day to check the timetable on. (eg: Thursday)")
	parser.add_argument('-t', '--time', default='', required=False, help="The time the venue must be empty. (eg: 15:30)")
	parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
                    
	args = parser.parse_args()

	time = args.time
	day = args.day

	if args.time == '':
		time = datetime.datetime.now().strftime('%H:%M')

	if args.day == '':
		day = datetime.datetime.now().strftime('%A')


	htmlRequest = requests.get('http://upnet.up.ac.za/tt/hatfield_timetable.html')

	timeTableObject = timetable.getTimetableFromHTML(htmlRequest.text)
	venueList = timetable.getVenueList(timeTableObject)

	filteredTimetable = timetable.getFilteredTimetable(day, time, timeTableObject)
	emptyVenues = timetable.getEmptyVenues(filteredTimetable, venueList)
	
	emptyVenues.sort()
	
	for venueName in emptyVenues:
		print(venueName)
		

#!/bin/python

__version__ = 'v1.0.0'

import argparse
import requests
import timetable
import datetime
import time
import exTime # Redundant.

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', '--day', default='', required=False, help="Day to check the timetable on. (eg: Thursday)")
	parser.add_argument('-t', '--time', default='', required=False, help="The time the venue must be empty. (eg: 15:30)")
	parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
	parser.add_argument('-l', '--length', default='1', help="Duration that the venue should be open in hours from the starting time. (eg: 1)")

	args = parser.parse_args()

	time = args.time
	day = args.day
	lengthOpen = args.length

	if args.time == '':
		time = datetime.datetime.now().strftime('%H:%M')

	if args.day == '':
		day = datetime.datetime.now().strftime('%A')


	htmlRequest = requests.get('http://upnet.up.ac.za/tt/hatfield_timetable.html')
	timeTableObject = timetable.getTimetableFromHTML(htmlRequest.text)
	venueList = timetable.getVenueList(timeTableObject)
	emptyVenuesListList = []
	emptyVenues = []

	for i in range(0,int(lengthOpen)):
		nTime = exTime.convertMinutesToTimeString(exTime.convertTimeStringToMinutes(time) + i*60)
		filteredTimetable = timetable.getFilteredTimetable(day, nTime, timeTableObject)
		emptyVenuesListList.insert(0, timetable.getEmptyVenues(filteredTimetable, venueList))

	# How we will be doing this is selecting list one as the base list and adding all elements which are not contained in the other lists to the final list.
	if(lengthOpen == '1'):
		for venueName in emptyVenuesListList[0]:
	 		print(venueName)
	
	for value in emptyVenuesListList[0]:
		for i in range(1,int(lengthOpen)):
			found = False
			for exValue in emptyVenuesListList[i]:
				if exValue == value:
					found = True
			if found and not(value in emptyVenues):
				emptyVenues.insert(0,value)

	emptyVenues.sort()
	for value in emptyVenues:
		print(value)

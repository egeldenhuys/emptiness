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
	parser.add_argument('-l', '--length', default='1', help="Duration that the venue should be open in hours from the starting time with a max of 4. (eg: 1)")

	args = parser.parse_args()

	time = args.time
	day = args.day
	lengthOpen = args.length
	if int(lengthOpen) > 4:
		lengthOpen = str(4)

	if args.time == '':
		time = datetime.datetime.now().strftime('%H:%M')

	if args.day == '':
		day = datetime.datetime.now().strftime('%A')


	htmlRequest = requests.get('http://upnet.up.ac.za/tt/hatfield_timetable.html')
	timeTableObject = timetable.getTimetableFromHTML(htmlRequest.text)

	# venueList = timetable.getVenueList(timeTableObject)
	# At this point we can start to apply filters to the timeTableObject

	for i in range(0,int(lengthOpen) + 1):
		timeTableObject = timetable.getFilteredTimetable(day,time,timeTableObject)


	for entry in timeTableObject:
		print(entry.venue)

import timetable
import exTime
import os
import datetime
import requests
import os
import time
import sys

def getHTML():
	pageBuffer = ''
	
	day = datetime.datetime.now().strftime('%A')
	timeA = datetime.datetime.now().strftime('%H:%M')
	#timeA = '10:00'
	
	emptyA = getEmptyVenuesFromURL('http://upnet.up.ac.za/tt/hatfield_timetable.html', day, timeA)
	
	# Add an hour to timeB
	# NOTE: Day overflow at 23:00
	
	timeB = exTime.convertTimeStringToMinutes(timeA)
	timeB = timeB + 60
	timeB = exTime.convertMinutesToTimeString(timeB)
	
	
	emptyB = getEmptyVenuesFromURL('http://upnet.up.ac.za/tt/hatfield_timetable.html', day, timeB)
	
	pageBuffer += '<!DOCTYPE html>\n<html>\n<head><title>Emptiness v1.0.0</title></head>\n<body>\n'
	
	pageBuffer += '<p style="font-family:courier, monospace;">\n'
	pageBuffer += 'Last update: ' + day + ' ' + timeA + '</p>\n'
	
	pageBuffer += '<table style="font-family:courier, monospace;">\n'
	pageBuffer += '<th> Block of ' + timeA + '</th><th>Block of ' + timeB + '</th>\n'
	
	if len(emptyA) > len(emptyB):
		# A is key
		for i in range(0, len(emptyB)):
			pageBuffer += '<tr><td>' + emptyA[i]+ '</td><td>' + emptyB[i] +  '</td></tr>\n'
			
		# B is now exhausted, continue with A
		
		for i in range(len(emptyB), len(emptyA)):
			pageBuffer += '<tr><td>' + emptyA[i] + '</td><td>' + ' ' +  '</td></tr>\n'
	else:
		# b is key
		for i in range(0, len(emptyA)):
			pageBuffer += '<tr><td>' + emptyA[i]+ '</td><td>' + emptyB[i] +  '</td></tr>\n'
			
		# A is now exhausted, continue with B
		
		for i in range(len(emptyB), len(emptyA)):
			pageBuffer += '<tr><td>' + ' ' + '</td><td>' + emptyB[i] +  '</td></tr>\n'
			
	pageBuffer += '</table>\n</body>\n</html>'
	
	return pageBuffer
		
def getEmptyVenuesFromURL(url, day, time):

	# TODO: Error handling
	htmlRequest = requests.get(url)

	timeTableObject = timetable.getTimetableFromHTML(htmlRequest.text)
	venueList = timetable.getVenueList(timeTableObject)

	filteredTimetable = timetable.getFilteredTimetable(day, time, timeTableObject)
	emptyVenues = timetable.getEmptyVenues(filteredTimetable, venueList)
	
	emptyVenues.sort()
	
	return emptyVenues
	
if __name__ == '__main__':
	
	abort = False
	
	if not os.path.exists('www'):
		os.mkdir('www')
	
	while True and not abort:
		print('Updating @ ' + str(datetime.datetime.now()))
		try:
			pageBuffer = getHTML()
		
			output = open('www/index.html', 'w')
			output.write(pageBuffer)
			output.close()
		
		except KeyboardInterrupt:
			raise
		except SystemExit:
			raise
		except Exception as e:
			print("Unexpected error:" + str(e))
		
		time.sleep(60)
		
		


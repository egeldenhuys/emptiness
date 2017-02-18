import timetable
import exTime
import os
import datetime
import requests
import os
import time
import sys
import cgi

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# Init timetable in memory

htmlFile = ''
lastUpdate = ''

@app.route('/')
def displayVenues():

	fullTime = datetime.datetime.now().strftime('%A %H:%M:%S')
	# Get time variables
	day = datetime.datetime.now().strftime('%A')
	timeA = datetime.datetime.now().strftime('%H:%M')
	timeB = exTime.convertTimeStringToMinutes(timeA)
	timeB = timeB + 60
	timeB = exTime.convertMinutesToTimeString(timeB)

	timeTableObject = timetable.getTimetableFromHTML(htmlFile)

	emptyA = timetable.getEmptyVenuesFromFullTimetable(day, timeA, timeTableObject)
	emptyB = timetable.getEmptyVenuesFromFullTimetable(day, timeB, timeTableObject)

	emptyA.sort()
	emptyB.sort()

	emptyC = getDualColumnList(emptyA, emptyB)

	return render_template('index.html', dualColumnList=emptyC, timeA=timeA, timeB=timeB, fullTime=fullTime, lastUpdate=lastUpdate), 200

@app.route('/update')
def updateTimetableInMemory_trigger():
	updateTimetableInMemory()
	return render_template('update.html'), 200

def updateTimetableInMemory():
	global htmlFile
	global lastUpdate

	htmlRequest = requests.get('http://upnet.up.ac.za/tt/hatfield_timetable.html')
	htmlFile = htmlRequest.text
	lastUpdate = datetime.datetime.now().strftime('%A %H:%M:%S')

# NOTE
updateTimetableInMemory()

@app.route('/flask_log')
def displayFlaskLog():
	f = open('flask-server.log', 'r')
	data = f.read()
	data = cgi.escape(data)
	f.close()

	return '<pre>' + data + '</pre>', 200

@app.route('/dns_log')
def displayDnsLog():
	f = open('dns.log', 'r')
	data = f.read()
	data = cgi.escape(data)
	f.close()

	return '<pre>' + data + '</pre>', 200

def getDualColumnList(listA, listB):
	listC = []

	# if len(listA) == 0:
	# 	for i in range(0, len(listB)):
	# 		listC.append(' ')
	# 		listC.append(listB[i])
	# 	return listC
	#
	# if len(listB) == 0:
	# 	for i in range(0, len(listA)):
	# 		listC.append(listA[i])
	# 		listC.append(' ')
	# 	return listC

	if len(listA) > len(listB):
		# Populate until B runs out
		for i in range(0, len(listB)):
			listC.append(listA[i])
			listC.append(listB[i])

		# B is now exhausted, continue with A
		for i in range(len(listB), len(listA)):
			listC.append(listA[i])
			listC.append(' ')
	else:
		# Populate until A runs out
		for i in range(0, len(listA)):
			listC.append(listA[i])
			listC.append(listB[i])

		# A is now exhausted, continue with B
		for i in range(len(listA), len(listB)):
			listC.append(' ')
			listC.append(listB[i])

	return listC

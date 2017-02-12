import exTime
import copy

# Data structures and functions used to parse html page and store in TimetableEntry classes.

# Structures
class TimetableEntry:

	def __init__(self, day, start, end, venue):
		self.day = day
		self.start = start
		self.end = end
		self.venue = venue

# Functions

def getFilteredTimetable(day, time, timetable):
	""" Filter the timetable based on day and time.

	Args:
		day: The day to return from the timetable. EG "Monday"
		time: The time string to use as a filter. EG "14:24"
		timetable: The list of TimetableEntry to apply the filter proccess

	Returns:
		A list of TimetableEntry that match the day and are in session during the given time
	"""
	# # Discard all entries that do not match the day
	# for entry in timetable:	# if we do this we discard all the entries
	# 	if entry.day == day:
	# 		matchingDateTimetable.append(entry)

	finalTimetable = []

	# Discard all entries that do not match the time range
	for entry in timetable:
		if entry.day == day:
			# Convert strings to minutes
			start = exTime.convertTimeStringToMinutes(entry.start[:-3])
			end = exTime.convertTimeStringToMinutes(entry.end[:-3])
			timeMins = exTime.convertTimeStringToMinutes(time)

			# If timeMins is in the range of entry, then the venue is active and we add it to the final timetable

			if timeMins in range(start, end + 1): #range does not exclude the max value
				finalTimetable.append(entry)

	###DEBUG_S
	###		print(str(timeMins) + ' is in range of ' + '[' + str(start) + ', ' + str(end) + ']')
	###	else:
	###		print('Dropping: ' + str(timeMins) + ' not in [' + str(start) + ', ' + str(end) + ']')
	###DEBUG_E

	###DEBUG_S
	###print('Classes running at ' + time)
	###for entry in finalTimetable:
	###	print(entry.start + ' -> ' + entry.end + '\t' + entry.day + '\t\t' + entry.venue)
	###DEBUG_E

	return finalTimetable

def getEmptyVenues(timetable, venueList):
	""" Return a list of empty venues

	Args:
		timetable: A list of TimetableEntry to search in
		venueList: A list containing all valid venues

	Returns:
		Returns a list of all venues that are empty
	"""

	# Creates a deep copy of the list
	empty = venueList[:]

	# Remove venues from the empty list if they exist in the timetable
	for entry in timetable:
		if entry.venue in empty:
			empty.remove(entry.venue)

			###DEBUG_S
			###print('Dropping: ' + entry.venue)
			###print('\t' + entry.day + ' ' + entry.start + ' -> ' + entry.end)
			###print('----')
			###DEBUG_E


	return empty

def getVenueList(timetable):
	""" Return a list of all unique venues from the timetable

	Args:
		timetable: A list of TimetableEntry to scrape venues from
	"""

	venueList = []

	# Add all unique venues from the timetable to the venue list
	for entry in timetable:
		if not entry.venue in venueList:
			venueList.append(entry.venue)

	return venueList

def getTimetableEntry(text):
	""" Attempt to extract a TimetableEntry from a formatted line of HTML

	Args:
		text: A line of HTML to parse.

	Index
	Returns:
		If the HTML line was a valid timetable entry:
			A TimetableEntry object containing the relevant iformation
		Else
			A TimetableEntry object with all values set to -1

	"""

	# HTML Format:
	# <tr><td>4/SOR 420/G01/B/L1</td><td>S2</td><td>Monday</td><td>12:30:00</td><td>14:30:00</td><td>Regsgebou/Law building 1-31</td></tr>

	# Some constants describing the index of data after splitting at '>'
	LENGTH = 15

	OPEN_TAG_INDEX = 0
	CLOSE_TAG_INDEX = 13

	DAY_INDEX = 6
	START_TIME_INDEX = 8
	END_TIME_INDEX = 10
	VENUE_INDEX = 12

	entry = TimetableEntry(-1, -1, -1, -1)

	rawData = text.split('>')

	# Validate the data to make sure it is what we are looking for
	if len(rawData) == LENGTH:
		if rawData[OPEN_TAG_INDEX] == '<tr' and rawData[CLOSE_TAG_INDEX] == '</tr':

			# Add info to array and strip the left over tags
			entry = TimetableEntry(rawData[DAY_INDEX].strip('</td'), rawData[START_TIME_INDEX].strip('</td'), rawData[END_TIME_INDEX].strip('</td'), rawData[VENUE_INDEX].strip('</td'))

	return entry

def getTimetableFromHTML(text):
	""" Parse a HTML file and return a list of Timetable Entry

	Args:
		text: The HTML timetable

	Returns:
		A list of TimetableEntry objects
	"""

	timetable = []

	rawData = text.split('\r\n')

	for line in rawData:
		entry = getTimetableEntry(line)

		if entry.day != -1:
			timetable.append(entry)

	return timetable

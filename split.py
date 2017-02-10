import requests
import timetable
import argparse



def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("-d", "--day", default='', help="Day to check the timetable on. eg: Thursday")
	parser.add_argument("-s", "--start", default='', help="The start time of the block. HH:MM:SS (24h)")

	args = parser.parse_args()



	htmlRequest = requests.get("http://upnet.up.ac.za/tt/hatfield_timetable.html")

	timeTableObject = timetable.parseHTMLFile(htmlRequest.text)

	# Method 1 ; Elimination
	venueList = timetable.getVenueList(timeTableObject)

	empty = timetable.getEmptyVenues(args.day, args.start, timeTableObject, venueList)

	for el in empty:
		print(el)


main()

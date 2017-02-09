import requests
import argparse

class TimetableEntry:

    def __init__(self, day, start, end, venue):
        self.day = day
        self.start = start
        self.end = end
        self.venue = venue

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--day", default='', help="Day to check the timetable on. eg: Thursday")
    parser.add_argument("-s", "--start", default='', help="The start time of the block. HH:MM:SS (24h)")

    args = parser.parse_args()



    htmlRequest = requests.get("http://upnet.up.ac.za/tt/hatfield_timetable.html")

    timetable = parseHTMLFile(htmlRequest.text)

    venueList = getVenueList(timetable)

    empty = getEmptyVenues(args.day, args.start, timetable, venueList)

    for el in empty:
        print(el)

    '''
    for el in timetable:
        print(el.venue)
    '''

def getEmptyVenues(day, startTime, timetable, venueList):
    """
    Given some paramaters, a timetable and venueList, return the empty venues
    """

    empty = venueList.copy()
    
    # Discard all that do not match the day
    for entry in timetable:
        if entry.day != day:
            timetable.remove(entry)

    # Discard all that do not match the start time
    for entry in timetable:
        if entry.start != startTime:
            timetable.remove(entry)

    # By now we have a timetable that contains only the venues that are FULL
    # If the venue is in the timetable, remove it from the final result

    # Display only venues that are in the venueList, but not the timetable
    for entry in timetable:
        if entry.venue in empty:
            empty.remove(entry.venue)

    return empty

def getVenueList(timetable):
    """ 
    Given a timetable (list of TimetableEntry), return a list of venues
    """

    venueList = []

    # TODO: Optimise!
    for entry in timetable:
        if not entry.venue in venueList:
            venueList.append(entry.venue)  

    return venueList

def parseLine(text):
    """
    Given a line of HTML, returns the Day, Start, End, Venue in an array, respectively.
    """

    info = []

    rawData = text.split('>')
    
    # Validate the data to make sure it is what we are looking for
    if len(rawData) == 15:
        if rawData[0] == '<tr' and rawData[13] == '</tr':
            # 6 = Day
            # 8 = Time Start
            # 10 = Time End
            # 12 = Venue
            
            # Cleanup the left over tags
            info = [rawData[6].strip('</td'), rawData[8].strip('</td'), rawData[10].strip('</td'), rawData[12].strip('</td')]

    return info

def parseHTMLFile(text):
    '''
    Given a HTML file, return TimetableEntry objects in an array
    '''

    timetable = []

    rawData = text.split('\r\n')

    for line in rawData:
        info = parseLine(line)

        if len(info) != 0:
            timetable.append(TimetableEntry(info[0], info[1], info[2], info[3]))

    return timetable

main()



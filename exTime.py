#!/bin/python

# Converts input of the form hh:mm into strictly minutes.
def convertTimeStringToMinutes( timeString ):
	pos = timeString.find(':')
	if pos == -1:
		return -1

	hours = timeString[ : pos ]
	minutes = timeString[ pos+1 : pos + 3]

	return int(hours) * 60 + int(minutes)


# Converts minutes into the form hh:mm
def convertMinutesToTimeString( minutes ):
	i_minutes = minutes % 60
	i_hours = minutes // 60 		#Because we want floor division.


	s_minutes = str(i_minutes)
	if len(s_minutes) == 1:
		s_minutes = '0' + s_minutes

	s_hours = str(i_hours)
	if len(s_hours) == 1:
		s_hours = '0' + s_hours

	return s_hours + ':' + s_minutes

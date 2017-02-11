'''
	Code which can be used to work with lists
'''


def splitList_UniqueRecurring(baseList, listList):
	newList = []
	for venue in baseList:
		Found = 0
		for anotherList in listList:
			for otherVenue in anotherList:
				if venue in otherVenue:
					Found = Found + 1
					continue
		
			if ( Found == len(listList) and not(venue in newList)) :
				newList.insert(0,venue)

	return newList

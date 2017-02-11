'''
 Using the python dict() structure collects tag associated with
 particular venues from a file.
'''

# Structures
class Tags:
	def __init__(self):
		self.internal_dict = dict()
	def addKeyValue(self,key,value):
		self.internal_dict[key] = value
	def getValue(self,key):
		return self.internal_dict.get(key)
	def getLength(self):
		return len(self.internal_dict)
	def addFile(self,filename):
		lines = [line.rstrip('\n') for line in open(filename)]
		for line in lines:
			# Split the keys and values ; man is this ugly
			spec_one = line.find('"')
			if spec_one == -1:
				continue

			spec_two = line.find('"',spec_one + 1)
			if spec_two == -1:
				continue

			spec_three = line.find('"',spec_two + 1)
			if spec_three == -1:
				continue

			spec_four = line.find('"',spec_three + 1)
			if spec_four == -1:
				continue
			key = line[spec_one+1:spec_two]
			value = line[spec_three+1:spec_four]
			self.addKeyValue(key,value)

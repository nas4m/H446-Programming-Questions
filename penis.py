def longest(string):
	c = 0
	maxC = 0
	for i in range(len(string)):
		if string[i] == "C":
			c += 1
			if c > maxC:
				maxC = c
		else:
			c = 0
	return(maxC)
			
string = "CCMCCCCLLCCC"
#print(longest(string))


def ocrLongest(string): #function longest(sequence)
	currentRun = 0
	biggestRun = 0
	for i in range(0, len(string)): #for i = 0 To sequence.length - 1
		if string[i] == "C": #if sequence.substring(i, 1) == "C" then
			currentRun = currentRun + 1
		else:
			if currentRun > biggestRun:
				biggestRun = currentRun
			#endif
			currentRun = 0
		#endif
	#next i
	return(biggestRun)
	
print(ocrLongest(string))
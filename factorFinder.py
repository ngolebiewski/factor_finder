factorDict = {}


def factorFinder(myInteger):
	factorSet = [];
	for i in range(1,myInteger+1):
		if myInteger % i == 0:
			factorSet.append(i)
	return factorSet


def addFactorsToDict(myInteger):
	factorDict[myInteger] = factorFinder(myInteger)
	return factorDict
	
	
def factorSetBuilder(maxInteger):
	for i in range (1, maxInteger+1):
		addFactorsToDict(i)
	return factorDict
		
		
def isFactorInDict(currentNumber):
	''' Checks if an integer is already in the Dictionary '''
	if currentNumber in factorDict: 
		return True
	else:
		return False


# def userInputLoop():
# 	x = True
# 
# 	while x == True:
# 		myInteger = input("\nEnter a number to factor: ")
# 		if myInteger.isnumeric():
# 			factorSet = (factorFinder(int(myInteger)))
# 			print(factorSet)		
# 	
# 			again = input("Another number (Y/N)?: ")
# 			again = again.lower()
# 	
# 			if again == "n":
# 				x = False
# 		else:
# 			print("That's not a number, try again!")
# 	
# 	print("Thank you and goodnight\n")



#This one with some dictionary logic to save computing.
def userInputLoop():
	x = True

	while x == True:
		myInteger = input("\nEnter a number to factor: ")
		if myInteger.isnumeric():
			myInteger = int(myInteger)
			
			#IF to spit out dictionary answer if the computer already figured it out		
			if isFactorInDict(myInteger):
				print("this is already in the dictionary: ", factorDict[myInteger])
			
			#Else find the factors
			else:
				factorSet = (factorFinder(myInteger))
				addFactorsToDict(myInteger)
				print(factorSet)		
	
	
	
	
			again = input("Another number (Y/N)?: ")
			again = again.lower()
	
			if again == "n":
				x = False
				
		else:
			print("That's not a number, try again!")
	
	print("Thank you and goodnight\n")
	

	
	
	
############################
# Tests
############################	
	
# print("tests")
# input("continue...")
# 
# print("factors being added to dictionary?")

# factorSetBuilder(1000)

# print("check factor builder boolean")
# print(isFactorInDict(3)) #should be True
# print(isFactorInDict(13)) #should be False


############################
# Run the user input loop!
############################

factorSetBuilder(1000)
userInputLoop()
		
			
	
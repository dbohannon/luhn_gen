#luhn_gen.py
#Generates all possible values that will pass the Luhn check given unmasked portions of PAN
#@Param PAN
#@Return string
#Example usage: python luhn_gen.py 123456XXXXXX1234

import sys
import math
import re

#PAN object definition
class PAN(object):
        first = ""
        middle = 0
        last = ""

#Create new PAN object
def initPAN(pFirst, pMiddle, pLast):
	pPAN = PAN()
	pPAN.first = pFirst
	pPAN.middle = pMiddle
	pPAN.last = pLast
	return pPAN

#checks to make sure that the PAN passes a luhn mod-10 checksum
def cardLuhnChecksumIsValid(card_number):
	sum = 0
	num_digits = len(card_number)
	oddeven = num_digits & 1

	for count in range(0, num_digits):
	    digit = int(card_number[count])

	    if not (( count & 1 ) ^ oddeven ):
		digit = digit * 2
	    if digit > 9:
		digit = digit - 9

	    sum = sum + digit

	return ( (sum % 10) == 0 )

#Iterates through possible PAN values
def iterateValues(pPAN):
	validValues = 0
	iterations = int(math.pow(10, len(pPAN.middle)))
	#determine how many zeros we need to pad based on mask length
	padding = '0' + str(len(arg1[1]))
	for x in range(0, iterations):
		#create testPAN by concatenating first, padding current iteration, and last as strings
		testPAN = pPAN.first+str(format(x,padding))+pPAN.last
		
		#if test PAN passes Luhn check, print to stdout
		if cardLuhnChecksumIsValid(testPAN):
			print testPAN 
			validValues += 1
	#print number of valid values passing Luhn check
	print "Number of possible values passing Luhn check: " + str(validValues)

#Exit if one and only one additional arg is not included from the command line
if len(sys.argv) != 2:
	sys.exit("Please include a masked PAN in the format '123456XXXXXX1234' \n Example: python luhn_gen.py 123456XXXXXX1234")

arg1 =  sys.argv[1]
arg1 = re.split("(X+)", arg1)
print arg1

thisPAN = initPAN(arg1[0],arg1[1],arg1[2])
iterateValues(thisPAN)


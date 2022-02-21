#import the functions
from random import seed
from random import randint
#the randint function generates a random int number
seed()
#the seed had a number in it. i took this out and left it blank so that it generates a different set
#of numbers each time

for _ in range(6):
	value = randint(0, 50)
	print(value)

#the function takes two numbers used as the ranges
#in this case the range is 0-50 (start,end)

#how do i stop the numbers being repeated???
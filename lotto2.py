#import the functions
from random import seed
from random import choice

#use the seed function to generate a random number (leave blank so it is diferent each time)
seed()

#create a sequence to generate a range of numbers that the computer can take from
#did not want them to take the number 0 so started at 1
sequence = [a for a in range(1,51)]

#the choice in sequence allows the computer to choose a number within the range
for _ in range(6):
	selection = choice(sequence)
	print(selection)

#how do i stop it repeating the numbers??
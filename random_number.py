from random import randint
from sys import argv, exit

#Checks -- for sanity.
if len(argv) < 3:
	exit("Usage: python random_number.py minimum maximum.")

if argv[1].isdigit==False or argv[2].isdigit==False:
	exit("Error: One of the supplied args is not digits.")

min=int(argv[1])
max=int(argv[2])

print(f"Generated random number between {min} and {max}: {str(randint(min, max))}.")

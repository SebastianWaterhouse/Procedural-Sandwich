import random, time, sys
import whatmake as what
import toppingchoose as topchoose

again = True

while again:
	cont = True
	toprint = "You got a " + what.nameof
	topchoose.choose()
	for var in topchoose.variables:
		print(var)
		toprint = toprint + var
	print(toprint)
	topchoose.variables = []
	againq = input("Do you want another one? Y/N: ")
	while cont:
		if againq.lower() == "n":
			again = False
			cont = False
		elif againq.lower() == "y":
			again = True
			cont = False
		else:
			cont = True
			againq = input("I'm sorry, I didn't understand that. Please only use the letters Y, for yes, or N, for no: ")
print("Exited with code 0")



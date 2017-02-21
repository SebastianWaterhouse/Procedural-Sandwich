import random
import whatmake as what

a = 0
variables = []
def choose():
	for b in what.variables:
		variables.append(random.choice(b))
choose()
print(variables)
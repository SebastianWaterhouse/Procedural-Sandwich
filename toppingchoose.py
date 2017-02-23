import random
import whatmake as what

variables = []
def choose():
	for b in what.variables:
		if what.variables[b] == "list":
			b = eval("what." + b)
			a = random.choice(b)
			variables.append(a)
		elif what.variables[b] == "dictlist":
			ba = "what." + b
			ba = eval(ba)
			a = random.choice(list(ba))
			variables.append(a)
			if b in what.controllers:
				what.controllers[b] = ba[a]
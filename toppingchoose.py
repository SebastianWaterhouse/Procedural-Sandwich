import random
import whatmake as what

variables = []
sentence = ""

vowels = ["a", "e", "i", "o", "u"]

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

def grammarcheck():
	global sentence
	if what.template[0] == "A ":
		term2 = what.template[1]
		var1 = variables[term2]
		if var1[0].lower() in vowels:
			sentence = "An "
		else:
			sentence = "A "

def makesentence():
	global sentence
	for d in what.template[1:]:
		if type(d) is int:
			d = variables[d]
		sentence = sentence + str(d)
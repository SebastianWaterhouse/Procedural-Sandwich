import toppingchoose as top

nameof = "game" #REQUIRED
variablesno = 4
interface = ["2D", "3D", "Isometric", "Text-based"]
types = {
 "Action":["2D", "3D", "Isometric", "Text-based"],
 "Adventure":["2D", "3D", "Isometric", "Text-based"],
 "Stealth":["2D", "3D", "Isometric"],
 "Puzzle":["2D", "3D", "Isometric", "Text-based"],
 "1st-Person Shooter":["3D"],
 "3rd-Person Shooter":["2D", "3D", "Isometric"],
 "Platformer":["2D", "3D", "Isometric"],
 "Point and Click":["2D", "3D"],
 "Management":["2D", "3D", "Isometric", "Text-based"]
}
artstyles = ["Cartoony", "Realistic", "Gritty", "8-Bit"]
genres = ["Sci-Fi", "Fantasy"]

variables = { #REQUIRED - SEE toppingchoose.py for valid types. If you want a new type, open an issue on Github.
	"types":"dictlist",
	"interface":"list",
	"artstyles":"list",
	"genres":"list"
}

controllers = { #REQUIRED
	"types":interface
}

varsy = list(variables)

def makeSentence():
	template = ["a " + 0 + " " + 2 + " " + 1 + " in a " + 3 + " setting."] #REQUIRED

#Controllers MUST go before what they control AND be a dict containing values matching up to what is in what they control.
import random, time, sys

class flavors(object):
    def __init__(self, name, goes_with, favored_heat):
        self.name = name
        self.goes_with = goes_with
        self.favored_heat = favored_heat
umami = flavors(name = "umami", goes_with = ["spicy", "tangy", "salty", "bitter", "sweet"], favored_heat = 1)
savory = flavors(name = "savory", goes_with = ["leafy", "salty", "spicy", "sweet"], favored_heat = 1)
tangy = flavors(name = "tangy", goes_with = ["umami", "spicy", "eggy", "salty", "bitter"], favored_heat = 2)
spicy = flavors(name = "spicy", goes_with = ["tangy", "leafy", "savory", "umami", "salty"], favored_heat = 2)
bitter = flavors(name = "bitter", goes_with = ["umami", "spicy", "tangy", "salty"], favored_heat = 2)
salty = flavors(name = "salty", goes_with = ["umami", "spicy", "savory", "eggy", "bitter", "salty"], favored_heat = 0)
sweet = flavors(name = "sweet", goes_with = ["tangy", "eggy", "savory", "salty", "umami"], favored_heat = 0)
eggy = flavors(name = "eggy", goes_with = ["salty", "sweet"], favored_heat = 0)

vowels = {"a", "e", "i", "o", "u"}
ameats={"beef":umami, "hard_boiled_egg_slice":eggy, "porkchop":savory, "bologna":tangy, "chicken":umami, "salami":tangy, "ham":umami, "turkey":savory, "andouille_sausage":spicy}
acheeses={"cheddar":tangy, "swiss":savory, "blue":tangy, "feta":salty, "goat":tangy, "havarti":sweet, "provolone":salty, "gouda":sweet, "colby":sweet}
breads=["white", "pretzel", "baguette", "potato", "dark", "curry", "tortilla", "croissant"]
avegetables={"lettuce":bitter, "tomato":sweet, "onion":bitter, "pickle":salty, "avocado":eggy}
fillings=["m", "c", "v", "m c", "v c", "v m", "v m c"]
heats={0:"", 1:"heated_up ", 2:"toasted "}


again=1
unlock_special_weird=0

while again==1:
    meats = ameats.copy()
    vegetables = avegetables.copy()
    cheeses = acheeses.copy()
    grammar = 0
    grammara = "a"
    filling = ""
    bread = "".join(random.sample(list(breads), 1))
    meata = random.sample(list(meats), 1)
    meat = "".join(meata)
    filling = filling + meat
    meatb = meats[meat]
    eliminatem = list(meatb.goes_with)
    eliminatemm = " ".join(eliminatem)
    meggiekiller = ""
    for meg in vegetables.keys():
        megs = str(vegetables[meg].name)
        if any(kill for kill in megs if megs not in eliminatem):
            meggiekiller = meggiekiller + " " + meg
    thingeel = 0
    gol = 1
    while gol == 1:
        try:
            del vegetables[meggiekiller.split()[thingeel]]
            thingeel = thingeel + 1
        except IndexError:
            gol = 0
    meesekiller = ""
    for mee in cheeses.keys():
        mees = str(cheeses[mee].name)
        if any(killkill for killkill in mees if mees not in eliminatem):
            meesekiller = meesekiller + " " + mee
    thingiel = 0
    go = 1
    heatedm = meatb.favored_heat
    probable = [heatedm]
    while go == 1:
        try:
            del cheeses[meesekiller.split()[thingiel]]
            thingiel = thingiel + 1
        except IndexError:
            go = 0

    try:
        vegetablea = random.sample(list(vegetables), 1)
    except ValueError:
        vegetablea = "tomato"
        vegetables["tomato"] = sweet
    vegetable = "".join(vegetablea)
    filling = filling + ", " + vegetable
    vegetableb = vegetables[vegetable]
    eliminatev = list(vegetableb.goes_with)
    veesekiller = ""
    for vee in cheeses.keys():
        vees = str(cheeses[vee].name)
        if any(killkillkill for killkillkill in vees if vees not in eliminatev):
            veesekiller = veesekiller + " " + vee
    thingoel = 0
    gob = 1
    heatedv = vegetableb.favored_heat
    while gob == 1:
        try:
            del cheeses[veesekiller.split()[thingoel]]
            thingoel = thingoel + 1
        except IndexError:
            gob = 0
    probable = [heatedv]

    try:
        cheesea = random.sample(list(cheeses), 1)
    except ValueError:
        cheesea = ["cheddar"]
        cheeses["cheddar"] = tangy
    cheese = "".join(cheesea)
    filling = filling + ", and " + cheese
    cheeseb = cheeses[cheese]
    heatedc = cheeseb.favored_heat
    filling = filling + " cheese"

    probable = [heatedc]
    probable = sum(probable)/len(probable)
    probable = round(probable)

    heated = heats[int(probable)]

    importance = heated + filling
    importance = importance.replace("_", " ")

    if importance[0] in vowels:
        grammar = 1
    if grammar == 0:
        grammara = "a "
    if grammar == 1:
        grammara = "an "

    print("You got " + grammara + importance + " sandwich on " + bread + " bread!")
    time.sleep(1)
    again_a = input("Go again? Type N for no, or anything else for yes. ")
    again_a = again_a.lower()
    if again_a == "n":
        again=0
        sys.exit("Exited with code 0")

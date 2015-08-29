import random, time, sys

again=1
unlock_special_weird=0

vowels = ["a", "e", "i", "o", "u"]
meats=["beef", "porkchop", "bologna", "chicken", "salami", "sausage", "ham", "turkey"]
weirdmeats=["soylent green", "vortex meat", "frog meat", "rattlesnake meat", "spam", "crawdad meat", "racoon meat", "kangaroo meat", "pheasant meat", "opossum meat", "oyster", "clam", "gizzard", "hamster meat", "horse meat"]
cheeses=["cheddar", "swiss", "blue", "feta", "goat", "havarti", "provolone", "pepper jack", "gouda", "limburger", "colby"]
weirdcheeses=["scream", "vortex", "soy", "brown", "almond", "mini"]
breads=["white", "pretzel", "baguette", "potato", "dark", "curry", "tortilla", "croissant"]
weirdbreads=["vortex bread", "plywood", "surfboard", "graham cracker", "pancake", "waffle", "styrofoam", "bacon"]
vegetables=["lettuce", "tomato", "bean sprout", "onion", "pickle", "avocado"]
weirdvegetables=["brussel sprout", "green bean", "vortex veggie"]
fillings=["m", "c", "v", "m c", "v c", "v m", "v m c"]
heats=["heated up ", "", "toasted "]
weirdheats=["literally on fire ", "absolute 0 ", "broiled ", "wet ", "suveed "]
weirds = weirdmeats + weirdcheeses

weirdss = " ".join(weirds)
weirdbreadss = " ".join(weirdbreads)

while again==1:
    grammar = 0
    if unlock_special_weird==1:
        meats = meats + weirdmeats
        cheeses = cheeses + weirdcheeses
        vegetables = vegetables + weirdvegetables
        breads = breads + weirdbreads
        heats = heats + weirdheats
        unlock_special_weird = 2
    if unlock_special_weird==3:
        meats = list(set(meats) - set(weirdmeats))
        cheeses = list(set(cheeses) - set(weirdcheeses))
        vegetables = list(set(vegetables) - set(weirdvegetables))
        breads = list(set(breads) - set(weirdbreads))
        heats = list(set(heats) - set(weirdheats))
        unlock_special_weird=0
    heated = random.choice(heats)
    filling_type_s = random.choice(fillings)
    filling_type_l = len(filling_type_s.replace(" ", ""))
    filling = ""
    if "m" in filling_type_s:
        meat = random.choice(meats)
        filling = filling + meat
        if meat[0] in vowels: grammar = 1
    if "v" in filling_type_s:
        vegetable = random.choice(vegetables)
        if filling_type_l >= 2:
            if filling_type_l >=3:
                filling = filling + ", "
            elif "m" in filling_type_s:
                filling = filling + " and "
            else:
                if vegetable in vowels: grammar = 1
        else:
            if vegetable in vowels: grammar = 1
        filling = filling + vegetable
    if "c" in filling_type_s:
        cheese = random.choice(cheeses)
        if filling_type_l >= 2:
            if filling_type_l == 3:
                filling = filling + ", and "
            else:
                filling = filling + " and "
        else:
            if cheese[0] in vowels: grammar = 1
        filling = filling + cheese
    bread = random.choice(breads)
    if "c" in filling_type_s:
        filling = filling + " cheese"

    if any(word in weirdss for word in filling.split()):
        print("Warning! Weird Toppings!")
        time.sleep(2)
    if any(wordb in weirdbreads for wordb in bread.split()):
        print("Warning! Weird Bread!")
        time.sleep(2)
    if any(wordh in weirdheats for wordh in heated.split()):
        print("Warning! Weird Heat/Texture!")
        time.sleep(2)

    if unlock_special_weird == 2:
        if heated in (heats[4]): grammar = 1
        if heated not in (heats[4]): grammar = 0
    if heated not in (heats[1]): grammar = 0

    if grammar == 0:
        grammara = "a "
    if grammar == 1:
        grammara = "an "

    print("You got " + grammara + heated + filling + " sandwich on " + bread + " bread!")
    time.sleep(1)
    again_a = input("Go again? Type Y for yes, N for no, or type S to toggle Special Weirdness Mode! ")
    again_a = again_a.lower()
    if again_a == "d":
        print("Printing debug stuff...")
        try:
            print(vegetable)
        except NameError:
            pass
        try:
            print(meat)
        except NameError:
            pass
        try:
            print(bread)
        except NameError:
            pass
        try:
            if heated == "": print("No heating")
            else: print(heated)
        except NameError:
            pass
        try:
            print(grammar)
        except NameError:
            pass
        try:
            print(grammara)
        except NameError:
            pass
    elif again_a == "n":
        again=0
        sys.exit("Exited with code 0")
    elif again_a == "s":
        if unlock_special_weird==1:
            print("Special Weirdness Mode is now off!")
            unlock_special_weird=3
        else:
            print("Warning! Special Weirdness Mode stays the entire session, but the toppings have the same chance to appear as any other topping!")
            unlock_special_weird=1

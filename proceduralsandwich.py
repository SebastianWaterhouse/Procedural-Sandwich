import random, time, sys

again=1
unlock_special_weird=0

vowels = ["a", "e", "i", "o", "u"]
meats=["beef", "porkchop", "bologna", "chicken", "salami", "sausage", "ham", "turkey"]
weirdmeats=["soylent green", "vortex meat"]
cheeses=["cheddar", "swiss", "blue", "feta", "goat", "havarti", "provolone", "pepper jack", "gouda", "limburger"]
weirdcheeses=["scream", "vortex"]
breads=["white", "pretzel", "baguette", "potato", "dark", "curry", "tortilla"]
weirdbreads=["vortex bread", "plywood", "surfboard", "graham cracker", "pancake", "waffle"]
vegetables=["lettuce", "tomato", "bean sprout", "onion", "pickle", "avocado"]
weirdvegetables=["brussel sprout", "green bean", "vortex veggie"]
fillings=["m", "c", "v", "m c", "v c", "v m", "v m c"]
heats=["heated up ", "", "toasted "]
weirds = weirdmeats + weirdcheeses

weirdss = " ".join(weirds)
weirdbreadss = " ".join(weirdbreads)

while again==1:
    grammar = 0
    if unlock_special_weird==1:
        meats = meats + weirdmeats
        cheeses = cheeses + weirdcheeses
        vegetables = vegetables + weirdvegetables
        unlock_special_weird = 2
    if unlock_special_weird==3:
        meats = list(set(meats) - set(weirdmeats))
        cheeses = list(set(cheeses) - set(weirdcheeses))
        vegetables = list(set(vegetables) - set(weirdvegetables))
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

    if heated not in heats[1]: grammar = 0

    if grammar == 0:
        grammara = "a "
    if grammar == 1:
        grammara = "an "

    print("You got " + grammara + heated + filling + " sandwich on " + bread + " bread!")
    time.sleep(1)
    again_a = input("Go again? Type Y for yes, N for no, or type S to toggle Special Weirdness Mode! ")
    again_a = again_a.lower()
    if again_a == "n":
        again=0
        sys.exit("Exited with code 0")
    elif again_a == "s":
        if unlock_special_weird==1:
            print("Special Weirdness Mode is now off!")
            unlock_special_weird=3
        else:
            print("Warning! Special Weirdness Mode stays the entire session, but the toppings have the same chance to appear as any other topping!")
            unlock_special_weird=1

    if "v" in filling_type_s: del vegetable
    if "m" in filling_type_s: del meat
    if "c" in filling_type_s: del cheese

import random, time, sys
import toppings as top

again=1
unlock_special_weird=0

weirds = top.weirdmeats + top.weirdcheeses

weirdss = " ".join(weirds)
weirdbreadss = " ".join(top.weirdbreads)

while again==1:
    grammar = 0
    if unlock_special_weird==1:
        top.meats = top.meats + top.weirdmeats
        top.cheeses = top.cheeses + top.weirdcheeses
        top.vegetables = top.vegetables + top.weirdvegetables
        top.breads = top.breads + top.weirdbreads
        top.heats = top.heats + top.weirdheats
        unlock_special_weird = 2
    if unlock_special_weird==3:
        top.meats = list(set(top.meats) - set(top.weirdmeats))
        top.cheeses = list(set(top.cheeses) - set(top.weirdcheeses))
        top.vegetables = list(set(top.vegetables) - set(top.weirdvegetables))
        top.breads = list(set(top.breads) - set(top.weirdbreads))
        top.heats = list(set(top.heats) - set(top.weirdheats))
        unlock_special_weird=0
    heated = random.choice(top.heats)
    filling_type_s = random.choice(top.fillings)
    filling_type_l = len(filling_type_s.replace(" ", ""))
    filling = ""
    if "m" in filling_type_s:
        meat = random.choice(top.meats)
        filling = filling + meat
        if meat[0] in top.vowels: grammar = 1
    if "v" in filling_type_s:
        vegetable = random.choice(top.vegetables)
        if filling_type_l >= 2:
            if filling_type_l >=3:
                filling = filling + ", "
            elif "m" in filling_type_s:
                filling = filling + " and "
            else:
                if vegetable in top.vowels: grammar = 1
        else:
            if vegetable in top.vowels: grammar = 1
        filling = filling + vegetable
    if "c" in filling_type_s:
        cheese = random.choice(top.cheeses)
        if filling_type_l >= 2:
            if filling_type_l == 3:
                filling = filling + ", and "
            else:
                filling = filling + " and "
        else:
            if cheese[0] in top.vowels: grammar = 1
        filling = filling + cheese
    bread = random.choice(top.breads)
    if "c" in filling_type_s:
        filling = filling + " cheese"

    if any(word in weirdss for word in filling.split()):
        print("Warning! Weird Toppings!")
        time.sleep(2)
    if any(wordb in top.weirdbreads for wordb in bread.split()):
        print("Warning! Weird Bread!")
        time.sleep(2)
    if any(wordh in top.weirdheats for wordh in heated.split()):
        print("Warning! Weird Heat/Texture!")
        time.sleep(2)

    if unlock_special_weird == 2:
        if heated in (top.heats[4]): grammar = 1
        if heated not in (top.heats[4]): grammar = 0
    if heated not in (top.heats[1]): grammar = 0

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

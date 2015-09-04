import random, time, sys
from PIL import Image, ImageDraw

vowels = {"a", "e", "i", "o", "u"}
meats={"beef":"beef.png", "hard_boiled_egg_slice":"egg.png", "salami":"salami.png"}
cheeses={"cheddar":"cheddar.png"}
breads={"white":"white.png", "potato":"white.png", "dark":"dark.png"}
vegetables={"lettuce":"lettuce.png", "tomato":"tomato.png", "pickle":"pickle.png", "avocado":"avocado.png"}
heats={0:"", 1:"heated_up ", 2:"toasted "}

meat_size=(0, 7, 8, 8)
bread_size=(0, 6, 8, 8)
size = (8, 7)

again=1
unlock_special_weird=0

while again==1:
    grammar = 0
    grammara = "a"
    filling = ""
    meat = random.choice(list(meats))
    cheese = random.choice(list(cheeses))
    bread = random.choice(list(breads))
    vegetable = random.choice(list(vegetables))
    meatp = Image.open(meats[meat])
    meatp = meatp.crop(meat_size)
    cheesep = Image.open(cheeses[cheese])
    cheesep = cheesep.crop(meat_size)
    breadp = Image.open(breads[bread])
    breadp = breadp.crop(bread_size)
    vegetablep = Image.open(vegetables[vegetable])
    vegetablep = vegetablep.crop(meat_size)
    out = Image.new("RGBA", size, color=0)
    out.paste(breadp, (0, 0), breadp)
    out.paste(vegetablep, (0, 2), vegetablep)
    out.paste(cheesep, (0, 3), cheesep)
    out.paste(meatp, (0, 4,), meatp)
    out.paste(breadp, (0, 5), breadp)
    out = out.resize((512, 256))
    out.save("out.png")
    filling = meat + ", " + vegetable + ", and " + cheese + " cheese"


    heated = heats[random.choice(list(heats))]

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
    again_a = input("Go again? Type N for no, S to show your picture, or anything else for yes. ")
    again_a = again_a.lower()
    if again_a == "n":
        again=0
        sys.exit("Exited with code 0")
    if again_a == "s":
        out.show()

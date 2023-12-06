
import random

# skaicius = random.randint(1,20000)
# ivesta = input("Įveskite skaičių: ")

nuo = int(input("Pasirink skaičių nuo kurio žaisim: "))
iki = int(input("Paisrink skaičių iki kurio žaisim: "))
skaicius = random.randint(nuo, iki)
# print(skaicius)
kartai = 0
# nuo = nuo
# iki = iki

while True:
    print("Spėk tarp ", nuo, "ir", iki)
    ivesta = int(input("Įveskite skaičių: "))
    kartai +=1
    if ivesta > skaicius:
        if ivesta < nuo or ivesta > iki:
            print("Pasirinkite skaičių ribose")
        else:
            print("Tavo skaičius yra didesnis")
            iki = ivesta

    elif ivesta < skaicius:
        if ivesta < nuo or ivesta > iki:
            print("Pasirinkite skaičių ribose")
        else:
            print("Tavo skaičius mažesnis")
            nuo = ivesta
    else:
        print()
        print("Tu laimėjai!!")
        break
print()
print("Žaidimas baigtas")

print("Spėjimų skaičius: ", kartai)
print("Norėdami baigti žaidimą, spauskite ENTER")




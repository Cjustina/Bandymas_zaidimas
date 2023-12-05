
import random

# skaicius = random.randint(1,20000)
# ivesta = input("Įveskite skaičių: ")

nuo = int(input("Pasirink skaičių nuo kurio žaisim: "))
iki = int(input("Paisrink skaičių iki kurio žaisim: "))
skaicius = random.randint(nuo, iki)
# print(skaicius)
kartai = 0
d1 = nuo
d2 = iki

while True:
    print("Spėk tarp ", d1, "ir", d2)
    ivesta = int(input("Įveskite skaičių: "))
    kartai +=1
    if ivesta > skaicius:
        print("Tavo skaičius yra didesnis")
        d2 = ivesta
    elif ivesta < skaicius:
        print("Tavo skaičius mažesnis")
        d1 = ivesta
    else:
        print()
        print("Tu laimėjai!!")
        break
print()
print("Žaidimas baigtas")

print("Spėjimų skaičius: ", kartai)
input("Norėdami išeiti, spauskite ENTER")





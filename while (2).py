from random import randint

n = int(input())
s = 0
while n > 0:
    n -= 1
print(s)

pr = 3
liczba = randint(1,100)
licznik = 0
print(liczba)
while licznik < pr:
    inp = int(input())
    licznik += 1
    if liczba == inp:
        print("zgadles")
        break
    elif inp < liczba:
        print("za mala")
    else:
        print("za wielka")


a = int(input())
b = int(input())
if b == 0:
    print("nie dzielimy przez 0")
else:
    print(a/b)
    print(a//b)
    print(a%b)

pa = 0
nie_pa = 0
while True:
    inp = int(input())
    if inp == 0:
        break
    elif inp % 2 == 0:
        pa += 1
    else:
        nie_pa += 1
print(pa)
print(nie_pa)
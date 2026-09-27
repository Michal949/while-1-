i = 0
while True:
    print(f"i = {i}")
    i += 1
    # i = i + 1

import time

n = int(input())
while n > 0:
    time.sleep(1)
    print(f"n = {n}")
    n -= 1


import time

n = int(input())
while n > 0:
    if n % 2 != 0 and n % 7 == 0:
        print(n)
        n -= 1

n = int(input())
while n > 0:
    print(f"2^{n} = {2**n}")
    n -= 1

n = input()
while True:
    print("a - prostokat b - zakoncz program")
    inp = input(": ")
    if inp == "a":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"a*b = {a*b}")
    elif inp == "b":
        print("program zakonczyl dzialanie")
    else:
        print("nie ma takiej komendy")

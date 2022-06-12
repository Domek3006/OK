import random

fi = open(input("Podaj nazwę pliku do utworzenia: ").strip(), "w")
while True:
    n = input("Podaj liczbę wierzchołków: ").strip()
    if (n.isnumeric):
        n = int(n)
        if (n < 1):
            print("Liczba wierzchołków powinna wynosić przynajmniej 1.")
            continue
        break
    print("Podana wartość powinna być liczbą.")

i, j = list(map(float, input("Podaj przedział współrzędnych, np. 3 8: ").split()))
inst = [str(n)]
while True:
    fl = input("Współrzędne całkowite? [y/n] ").strip()
    if (fl == 'y'):
        fl = False
        break
    elif (fl == 'n'):
        fl = True
        break
    print("Odpowiedź powinna być formatu: [y/n]")
for o in range(n):
    if fl:
        x, y = random.uniform(i, j), random.uniform(i, j)
        x, y = round(x,2), round(y,2)
        inst.append("\n" + str(o+1) + " " + str(x) + " "+ str(y))
    else:
        while True:
            x, y = random.randint(i, j), random.randint(i, j)
            wr = "\n" + str(o+1) + " " + str(x) + " "+ str(y)
            if (wr not in inst):
                inst.append(wr)
                break
fi.writelines(inst)
fi.close()
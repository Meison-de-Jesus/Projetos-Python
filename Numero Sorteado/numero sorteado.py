import random
cont = 1


def sorteio():
    sort = random.randint(1, 6)
    return sort


value_sorted = sorteio()
print(value_sorted)

while cont >= 0:
    print(f"Você tem {(cont+1)} chance(s) ".upper())
    adv = input("Adivinhe qual o valor sorteado".upper().strip())
    if not adv.isdigit():
        continue
    else:
        adv_convertido = int(adv)
        if value_sorted == adv_convertido:
            print("O valor {} foi sorteado".format(
                value_sorted).upper().strip())
            cont = -1
        else:
            if cont >= 0:
                cont -= 1
else:
    print("Programa finalizado".upper().strip())

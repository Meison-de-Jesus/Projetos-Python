palavra = input("Informe a palavra secreta: ".upper())
acertos = list(range(0, len(palavra)))
acertos_acumulador = list(range(0, len(palavra)))
if palavra.isdigit():
    print("Você digitou um número".upper())
else:
    while True:
        cont_1 = 0  # Percorre a lista acertos
        letra = input("Informe uma letra existente na palavra: ".upper())
        if letra.upper() or letra.lower():
            for iterador in palavra:  # itera a palavra secreta
                if letra != iterador:
                    acertos[cont_1] = "*"
                    cont_1 += 1
                    continue
                else:
                    acertos[cont_1] = letra
                    cont_1 += 1
            cont_2 = 0
            for iterador in acertos:  # Itera acertos e insere o elemento "iterador" em acertos_acumulador
                if iterador != "*":
                    acertos_acumulador.insert(cont_2, letra)
                    del(acertos_acumulador[cont_2+1])
                    cont_2 += 1
                else:
                    cont_2 += 1
            if list(palavra) == acertos_acumulador:
                break
            else:
                continue
        print(acertos_acumulador)
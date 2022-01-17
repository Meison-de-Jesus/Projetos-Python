Q1 = {"pergunta": "Qual o ano de nascimento do Bahia ?",
      "resposta": {"a)": 1931, "b)": 1970, "c)": 2000}}


def printf():
    for keys, values in Q1.items():
        if keys != "resposta":
            print("{0}: {1}".format(keys, values))
        else:
            for chave, valor in Q1["resposta"].items():
                print(chave, valor)


printf()
booleano = True
while booleano:
    opcao = input("Informe qual a alternativa correta:")
    if not opcao.isdigit():
        print("por valor,informe uma opcao válida!".upper())
    else:
        opcao_ = int(opcao)
        if opcao_ == Q1["resposta"]["a)"]:
            print("Você acertou.", "parabéns!".upper())
            booleano = False
        else:
            print("Você errou.", "tente mais uma vez!".upper())
            continue
else:
    print("programa finalizado.".capitalize())

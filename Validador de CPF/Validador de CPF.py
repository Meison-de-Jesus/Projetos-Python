# Variáveis e Listas
CPF = "16899535009"
soma = 0
decr = 3
l1_CPF = list(range(0, 11))
l2_CPF = list(range(0, 11))  # Modificado em l2_CPF[9] e l2_CPF[10]
while decr:
    CPF_ = input("Informe seu CPF: ".strip())
    if not CPF.isnumeric() or not (len(CPF_) == 11):
        decr -= 1
        print("informe um CPF válido! Você tem mais {} tentativa(s)".format(decr).upper())
    else:
        decr = False
        continue
else:
    for indice, conteudo in enumerate(CPF_):
        l1_CPF[indice] = conteudo
        l2_CPF[indice] = conteudo
    # digito 1
    for indice, conteudo in enumerate(range(10, 1, -1)):
        mult = conteudo * int(l1_CPF[indice])
        soma += mult
    else:
        if (11 - (soma % 11)) > 9:
            l2_CPF[9] = 0
        else:
            l2_CPF[9] = 11 - (soma % 11)
    # digito 2
    soma = 0
    for indice, conteudo in enumerate(range(11, 1, -1)):
        mult = conteudo * int(l1_CPF[indice])
        soma += mult
        # print(soma)
    else:
        if (11 - (soma % 11)) == 9:
            l2_CPF[10] = 9
        else:
            l2_CPF[10] = 2
if CPF == str(l2_CPF):
    print("cpf válido".upper())
else:
    print("cpf inválido".upper())
inc = 0
while True:
    num_1 = input("Informe um número: ")
    num_2 = input("Informe um outro número: ")

    if num_1.isdigit() and num_2.isdigit():
        num_1_ = float(num_1)
        num_2_ = float(num_2)
        op = input("Qual operação deseja escolher ?".capitalize())

        if op == "*" or op == "multiplicação" or op == "produto":
            print("{} é o resultado do produto".format(num_1_*num_2_))
            print(f"{num_1_+num_2_:.d}é o resultado da soma")
        elif op == "-":
            print(f"{num_1_-num_2_}é o resultado da subtração")
        elif op == "raiz":
            print(f'{num_1_}')
        else:
            print("{} é o resultado da divisão".format(num_1_/num_2_))

    else:
        print("Não são números")

    pergunta = input("Deseja continuar ?")
    if pergunta == "sim":
        inc = inc + 1
        continue
    else:
        break

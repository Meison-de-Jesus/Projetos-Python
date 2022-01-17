inc = 0
while True:
    num_1 = input("Informe um número: ")
    num_2 = input("Informe um outro número: ")

    if num_1.isdigit() and num_2.isdigit():
        num_1 = float(num_1)
        num_2 = float(num_2)
        op = input("Qual operação deseja escolher ?")

        if op == "*":
            print("{} é o resultado do produto".format(num_1*num_2))
        elif op == "+":
            print(f"{num_1+num_2}é o resultado da soma")
        elif op == "-":
            print(f"{num_1-num_2}é o resultado da subtração")
        elif op == "raiz":
            print(f'{num_1}')
        else:
            print("{} é o resultado da divisão".format(num_1/num_2))

    else:
        print("Não são números")

    pergunta = input("Deseja continuar ?")
    if pergunta == "sim":
        inc = inc + 1
        continue
    else:
        break
def gerador_tabuleiro():
    tabuleiro = list(range(0, 9))

    # Formatação do tabuleiro
    for iterador1 in tabuleiro:
        tabuleiro[iterador1] = []
        for iterador2 in range(0, 9):
            tabuleiro[iterador1].insert((iterador2), "-")

    # Linha e coluna de localização
    for iterador1 in tabuleiro:
        for iterador2, valor in enumerate(tabuleiro[0]):  # Linha 0
            tabuleiro[0][iterador2] = "" + str(iterador2)
    tabuleiro[0][0] = " "
    tabuleiro[1][0] = "A"
    tabuleiro[2][0] = "B"
    tabuleiro[3][0] = "C"
    tabuleiro[4][0] = "D"
    tabuleiro[5][0] = "E"
    tabuleiro[6][0] = "F"
    tabuleiro[7][0] = "G"
    tabuleiro[8][0] = "H"

    # Inserindo as peças brancas(B) e pretas(P)
    for iterador1, valor in enumerate(tabuleiro):
        if iterador1 >= 1 and iterador1 <= 3:
            for iterador2 in range(1, 9):
                valor[iterador2] = "p"
        elif iterador1 >= 6 and iterador1 <= 8:
            for iterador2 in range(1, 9):
                valor[iterador2] = "b"

    # Formata o tabuleiro em forma tabular
    for iterador1 in tabuleiro:
        print(iterador1)


booleano = True
while booleano:
    gerador_tabuleiro()
    numero_de_jogadores = input(
        "Informe 1 para jogar com o computador e 2 para jogar com usuário: ")

    if not numero_de_jogadores.isdecimal():
        print("Valor inválido".upper())
        continue
    else:
        if numero_de_jogadores == "1" or numero_de_jogadores == "2":
            if numero_de_jogadores == "1":
                ...
            else:
                ...
        else:
            print("Número inválido".title())
            continue
    booleano = False

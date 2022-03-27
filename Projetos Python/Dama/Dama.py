cont = 1
acumulator = 0

#  Gerando o tabuleiro
tabuleiro = list(range(0, 9))
for iterador_1 in tabuleiro:
    tabuleiro[iterador_1] = []
    for iterator_2 in range(0, 9):
        tabuleiro[iterador_1].insert((iterator_2), "x")
        ("\n")

tabuleiro[0][0] = " "

for iterador_1 in tabuleiro[0]:
    acumulator = acumulator + cont
    for iterator_2 in tabuleiro[0]:
        if acumulator <= 8:
            tabuleiro[0][acumulator] = "" + str(acumulator)
        else:
            pass

for iterador_1 in tabuleiro:
    acumulator = acumulator + cont
    if acumulator <= 8:
        tabuleiro[acumulator][0] = "A"
    else:
        pass


for iterator_1 in tabuleiro:
    for iterator_2 in iterator_1:
        pass
    print(iterator_1)

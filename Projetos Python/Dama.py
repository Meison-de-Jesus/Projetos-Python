cont = 1
acumulator = 0
#  Gerando o tabuleiro
tabuleiro = list(range(0, 9))
for iterator_1 in tabuleiro:
    tabuleiro[iterator_1] = []
    for iterator_2 in range(0, 9):
        tabuleiro[iterator_1].insert((iterator_2), "x")
        ("\n")

tabuleiro[0][0] = " "
for iterator_1 in tabuleiro[0]:
    acumulator = acumulator + cont
    for iterator_2 in tabuleiro[0]:
        if acumulator <= 8:
            tabuleiro[0][acumulator] = acumulator
        else:
            pass

for iterator_1 in tabuleiro:
    acumulator = acumulator + cont
    if acumulator <= 8:
        tabuleiro[acumulator][0] = acumulator
    else:
        pass


for iterator_1 in tabuleiro:
    for iterator_2 in iterator_1:
        pass
    print(iterator_1)

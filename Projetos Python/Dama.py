tabuleiro = list(range(0, 8))
for iterator_1 in tabuleiro:
    tabuleiro[int(iterator_1)] = []
    for iterator_2 in range(0, 8):
        tabuleiro[int(iterator_1)].insert(int(iterator_2), "x")
        ("\n")
for iterator_1 in tabuleiro:
    for iterator_2 in iterator_1:
        pass
    print(iterator_1)

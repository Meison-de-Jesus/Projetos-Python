import random
lista_master = []
# conjunto_repetidos = set()


def gerando_lista():  # Gera lista com 10 posições;
    for i in range(0, 10):
        lista_master.append("")
    return None


def adicionando_listaINlista():  # Adiciona uma lista vazia em cada índice;
    for i in range(0, 10):
        lista_master[i] = []
        # print(lista_master[i])
    return None


def gerador_numeros():  # Gera números aleatórios entre 1 e 10;
    for indice1 in lista_master:
        for indice2 in range(0, 10):
            indice1.append(random.randint(1, 10))
    return None


gerando_lista()
adicionando_listaINlista()
gerador_numeros()
for primeiro_indice, lista_interna in enumerate(lista_master):  # Muda de lista
    # Segura um número da lista(tem o índice fixo)
    conjunto_repetidos = set()
    for segundo_indice, numero_externo in enumerate(lista_interna):
        # Percorre cada valor da lista(tem o índice variando)
        for terceiro_indice, numero_interno in enumerate(lista_interna):
            if segundo_indice != terceiro_indice:
                if numero_externo == numero_interno:
                    conjunto_repetidos.add(numero_interno)
                else:
                    ...
            else:
                pass
    print(f"{lista_interna} -> {conjunto_repetidos}")

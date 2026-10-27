def lista_polaczona(lista_1: list, lista_2: list) -> bool:
    cala_lista = list(set(lista_1 + lista_2))
    wynikowa_lista = []
    for x in cala_lista:
        wynikowa_lista.append(x**3)
    return wynikowa_lista


print(lista_polaczona([1, 2, 3], [2, 3, 4]))

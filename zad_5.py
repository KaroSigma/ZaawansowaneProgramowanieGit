def czy_w_lista(lista: list, liczba: int) -> bool:
    for x in lista:
        if x == liczba:
            return True
    return False


print(czy_w_lista([1, 2, 3], 2))

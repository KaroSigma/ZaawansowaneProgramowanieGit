def czy_w_lista(lista: list, liczba: int) -> bool:
    for x in lista:
        if x == liczba:
            return True
    return False

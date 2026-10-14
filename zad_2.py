print("b zadanie")
def pomnoz_for(lista_num):
    nowa_lista = []
    for numer in lista_num:
        nowa_lista.append(numer * 2)
    return nowa_lista

def pomnoz_skladana(lista_num):
    return [numer * 2 for numer in lista_num]

lista_2 = [2, 4, 6, 8, 10]
wynik_1 = pomnoz_for(lista_2)
wynik_2 = pomnoz_skladana(lista_2)

print(wynik_1)  
print(wynik_2)  
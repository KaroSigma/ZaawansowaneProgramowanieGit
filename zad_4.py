print("\nd zadanie")
def co_drugi(liczby):
    for i in range(0, len(liczby), 2): 
        print(liczby[i])

parzyste_lista = list(range(10))
co_drugi(parzyste_lista)
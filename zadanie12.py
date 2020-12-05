def wartosc_koszyka (lista):
    suma=0
    for i in lista:
        suma+=i['wartosc']

    #Naliczenie obnizki 5% przy 3 rzeczach
    if len(lista) >= 2:
        suma=0.95*suma

    return suma

koszyk = [{'nazwa': 'jablka', 'wartosc': 2},
{'nazwa': 'gruszki', 'wartosc': 3},
{'nazwa': 'sliwki', 'wartosc': 2.5},
{'nazwa': 'mleko', 'wartosc': 2.5},
{'nazwa': 'ser', 'wartosc': 2.5}]

print(wartosc_koszyka(koszyk))

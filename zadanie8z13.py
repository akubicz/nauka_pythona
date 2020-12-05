koszyk = [{'nazwa': 'jablka', 'wartosc': 2},
{'nazwa': 'gruszki', 'wartosc': 3},
{'nazwa': 'sliwki', 'wartosc': 2.5}]
suma=0

for i in koszyk:
    suma+=i['wartosc']

print(suma)

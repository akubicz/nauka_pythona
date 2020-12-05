koszyk = [{'nazwa': 'jablka', 'wartosc': 2},
{'nazwa': 'gruszki', 'wartosc': 3},
{'nazwa': 'sliwki', 'wartosc': 2.5},
{'nazwa': 'mleko', 'wartosc': 2.5},
{'nazwa': 'ser', 'wartosc': 2.5}]
suma=0
check_ser=0
check_mleko=0

for i in koszyk:
    suma+=i['wartosc']
    if i['nazwa']=='ser': check_ser=1
    elif i['nazwa']=='mleko': check_mleko=1

if (check_ser == 1 and check_mleko == 1):
   suma = 0.9*suma
   print("UWAGA. Obnizka wartosci koszyka o 10%")

print("Wartosc koszyka {:.2f}".format(suma))

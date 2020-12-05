koszyk = {'nazwa': 'jablka', 'wartosc': 2}

print(koszyk['nazwa'])
print(koszyk['wartosc'])

for i in koszyk:
    print("{0}:{1}".format(i, koszyk[i]))

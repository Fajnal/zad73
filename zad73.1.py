with open("tekst.txt", "r") as plik:    #otworzenie pliku tekstowego
    for line in plik:
        slowa = line.split()            #rozdzielenie słów

odp = []

for word in slowa:
    znak = word[0]
    for char in word[1::]:
        if znak == char:
            odp.append(word)            #dodawanie słowa do tablicy "odp"
            break
        znak = char

print(format(len(odp)))                 #wypisanie ilości słów, w których występują dwie kolejne takie same litery
alfabet = {}
litery = 0

with open("tekst.txt", "r") as plik:        #otworzenie pliku tekstowego
    for line in plik:
        slowa = line.split()

def czestotliwosc(slowa):                   #funkcja uzupełniająca tablicę "alfabet" literami z pliku
    for znak in slowa:
        if znak not in alfabet:
            alfabet[znak] = 1
        else:
            alfabet[znak] += 1

odp = []

for word in slowa:
    znak = word[0]
    for char in word[1::]:
        if znak == char:
            odp.append(word)                #dodanie słowa do tablicy "odp"
            break
        znak = char
    czestotliwosc(word)                     #przywołanie funkcji "czestotliwosc"
    litery += len(word)

for litera in sorted(alfabet):
    print("{}: {} ({}%)".format(litera, alfabet[litera], round((alfabet[litera]/litery) * 100, 2)))
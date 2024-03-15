samogloski = "AEIOUY"
najdluzsze_podslowo = ""

with open("tekst.txt", "r") as plik:                                    #otworzenie pliku tekstowego
    for line in plik:
        slowa = line.split()

def znajdz_podslowo(slowo):                                             #funcja sprawdzająca, czy słowo zawiera podsłowo
    global najdluzsze_podslowo
    global podslowa
    podslowo = ""
    for znak in slowo:
        if znak not in samogloski:
            podslowo += znak
            if len(podslowo) >= len(najdluzsze_podslowo):
                if len(podslowo) > len(najdluzsze_podslowo):
                    podslowa = []
                najdluzsze_podslowo = podslowo
                if slowo not in podslowa:
                    podslowa.append(slowo)
        else:
            dlugosc = 0
            podslowo = ""

odp = []

for word in slowa:
    znak = word[0]
    for char in word[1::]:
        if znak == char:
            odp.append(word)                                                #dodanie słowa do tablicy "odp"
            break
        znak = char
    znajdz_podslowo(word)                                                   #przywołanie funkcji "znajdz podslowo"

print("Długość najdłuższego podsłowa: {}\nPierwsze slowo to {}\nŁącznie jest ich {}".format(len(najdluzsze_podslowo), podslowa[0], len(podslowa)))
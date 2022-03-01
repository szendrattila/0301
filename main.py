#Ausztria;1995.01.01
#Belgium;1958.01.01
"""
class Eu:
    def __init__(self, sor):
        orszag, datum = sor.strip().split(";")
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[:4])
        self.honap = int(datum[5:7])
        self.nap = int(datum[8:10])
lista = []
with open ("EUcsatlakozas.txt", encoding = "latin2") as f:
    for sor in f:
        lista.append(Eu(sor))
#3. feladat
print(f"3. feladat: EU tagállamainak száma {len(lista)}")

#4.feladat
csatlakozas = len([sor for sor in lista if sor.ev == 2007])
print(f"4. feladat: 2007-ben {csatlakozas} ország csatlakozott ")
#5. feladat
magyar = [sor.datum for sor in lista if sor.orszag == "Magyarország"]
print(f"5. feladat: Magyarország csatlakozásának dátuma : {magyar[0]}")
#6. feladat
volte = len([sor for sor in lista if sor.honap == 5])
if volte > 0:
    print("6. feladat: Májusban volt csatlakozás")
else:
    print("6. feladat: Májusban nem volt castlakozás")

#elso proba -----------------------------------------------------------------------
    
#7. feladat:
utoljara = max(lista, key=lambda x:x.datum).orszag
print(f"7. feladat Legutoljara csatlakozott orszag: {utoljara}")
#8. feladat
stat = dict()
for sor in lista:
    stat[sor.ev] = stat.get(sor.ev, 0) + 1
for kulcs, ertek in stat.items():
    print(f"        {kulcs} - {ertek} ország")

"""

#################################################################################
#Ausztria;1995.01.01
#Belgium;1958.01.01
class Eu:
    def __init__(self, sor):
        orszag, datum = sor.strip().split(";")
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[:4])
        self.honap = int(datum[5:7])
        self.nap = int(datum[8:10])
lista = []
with open ("EUcsatlakozas.txt", encoding="latin2") as f:
    for sor in f:
        lista.append(Eu(sor))

#3. feladat
print(f"3. feladatEU tagállamainak száma: {len(lista)}")
#4.feladat
csatlakozas = len([sor for sor in lista if sor.ev == 2007])
print(f"4. feladat:2007-ben {csatlakozas} ország csatlakozott")
#5. feladat
magyar = [sor.datum for sor in lista if sor.orszag == "Magyarország"]
print(f"5. feladat: Magyarország csatlakozásának dátuma: {magyar[0]}")
#6. feladat
volte = len([sor for sor in lista if sor.honap == 5])
if volte > 0:
    print("6. feladat: volt csatlakozás májusban")
if volte <= 0:
    print("6. feladat: nem volt csatlakozás májusban")
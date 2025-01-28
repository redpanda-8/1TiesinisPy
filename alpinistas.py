# Tiesinis algoritmas
# 1. Alpinistas i kalno virsune kope x1 savaiciu ir y1 paru, o leidosi x2 savaiciu ir y2 paru.
# Parasykite programa, kuri apskaiciuotu, kiek savaiciu ir paru truko alpinisto kelione?
# Pasitikrinkite: Kai:
# x1 = 3 
# y1 = 5
# x2 = 4
# y2 = 6
# Turi buti atspausdinta "Alpinistas keliavo 8 savaites ir 4 paras."
x1 = 3  # savaites lipo
y1 = 5  # dienas lipo
x2 = 4  # savaites leidosi
y2 = 6  # dienas leidosi

# sulyginam matavima (kad butu dienos visur)
kiekDienu_lipo = (x1 * 7) + y1  # dienas lipo
kiekDienu_leidosi = (x2 * 7) + y2  # dienas leidosi

# suma kiek isviso truko kelione
dienu_suma = kiekDienu_lipo + kiekDienu_leidosi

# pakeiciam matavima (kad vel butu savaites+dienos visur)
kiekSavaiciu = dienu_suma // 7  # dalinam kad gauti savaites
kiekDienu = dienu_suma % 7  # liekana kiek liko dienu

print(f"Alpinistas keliavo {kiekSavaiciu} savaites ir {kiekDienu} dienas.")
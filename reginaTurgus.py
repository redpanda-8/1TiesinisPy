# Tiesinis algoritmas
# 2. Turguje liepu medaus kilogramas kainuoja a eur, grikiu - b eur, rapsu - c eur. Regina pirko
# aa kg liepu, bb kg grikiu ir cc kg rapsu medaus. Parasykite programa, kuri skaiciuoja kokia
# pinigyu suma s Regina sumokes uz medu, jeigu pardavejas pritaike n eur nuolaida.
# Pasitikrinkite: Kai:
# a = 6,5
# b = 8,5
# c = 6,5
# aa = 0,5
# bb = 1
# cc = 0,5
# n = 5
# s = 10 eur

a = 6.5  # kaina uz kilograma liepu medaus
b = 8.5  # kaina uz 1kg grikiu medaus
c = 6.5  # kaina uz 1kg rapsu medaus
aa = 0.5 # Regina pirko liepu kg
bb = 1   # Regina pirko grikiu kg
cc = 0.5 # Regina pirko rapsu kg
n = 5    # nuolaida

# kokia bendra kiekvieno medaus kaina (kaina uz kg * kiek pirko)
kaina_liepu = a * aa
kaina_grikiu = b * bb
kaina_rapsu = c * cc

kainaBeNuolaidos = kaina_liepu + kaina_grikiu + kaina_rapsu # kaina be nuolaidos
galutineKaina = kainaBeNuolaidos - n # kokia galutine kaina atemus nuolaida

print(f"Regina sumokes {galutineKaina} eurus.")
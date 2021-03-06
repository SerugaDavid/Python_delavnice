# KAJ SMO SE DO SEDAJ NAUČILI?

# RAČUNANJE IN OPERATORJI
# + seštevanje
print(2 + 3)  # 5
# - odštevanje
print(3 - 2)  # 1
# * množenje
print(2 * 3)  # 6
# / deljenje
print(5 / 2)  # 2.5
#
# nekaj dodatnih operatorjev
# // celoštevilčno deljenje
print(5 // 2)  # 2
# ** potenciranje
print(5 ** 2)  # 25
# % ostanek pri deljenju
print(5 % 2)  # 1

# BESEDILO
print("Navadno besedilo")  # besedilo z dvojnimi narekovaji "
print('Navadno besedilo')  # besedilo z enojnimi narekovaji '
print("Želimo 'uporabiti' enojne narekovaje v besedilu")  # potrebujemo, da jih obkrožijo dvojni narekovaji "
print('Želimo "uporabiti" dvojne narekovaje v besedilu')  # potrebujemo, da jih obkrožijo enojni narekovaji '
print("""Želimo uporabiti "dvojne" in 'enojne' narekovaje""")  # potrebujemo, da jih obkrižijo 3x dvojni ali enojni narekovaji """/'''
print("""To je prva vrsta,
to je druga vrsta,
to je tretja vrsta""")  # 3x dvojni narekovaji nam tudi omogočijo da pišemo več vrstično besedilo
print("Vrsta 1\nVrsta 2\nVrsta 3")  # prav tako nam novo vrsto omogoči znak \n

# LOGIČNI IZRAZI
# > večje
print(5 > 2)  # True
# < manjše
print(5 < 2)  # False
# == je enako
print(5 == 2)  # False
# != ni enako
print(5 != 2)  # True
# >= večje ali enako
print(5 >= 2)  # True
# <= manjše ali enako
print(5 <= 2)  # False

# SPREMENLJIVKE
# spremenljivke lahko poimenujemo kakorkoli
a = 5
b = 5
stevilka = 5
ksjdfksdnfgnasf = 5
# spremenljivke imajo lahko različne podatkovne tipe
a = 5
a = True
a = "pet"
# s spremenljivkami lahko delamo, kot bi delali z navadnimi podatki
print(stevilka + b)  # 10
print(a == ksjdfksdnfgnasf)  # False
print(a)  # pet
print(stevilka < b * ksjdfksdnfgnasf)  # True
# spremenljivkam lahko prirejamo vrednosti drugih spremeljivk
b = b ** stevilka
print(b)  # 125
a = a * stevilka
print(a)  # petpetpetpetpet
c = "a" * (b + stevilka)
print(c)  # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# IF STAVKI
# if stavki nam omogočijo, da poganjamo dele naše kode pogojno
# ti sprejmejo logični pogoj, to je lahko pogoj(a > b) ali trditev(True)
# če je pogoj pravilen izvedemo določeni del kode
a = 1
b = 2
if a > b:
    print("a je večji od b")
if a < b:
    print("b je večji od a")
if a == b:
    print("a in b sta enaka")
# if stavki nam omogočijo da izvajamo drugačno kodo, če pogoj NI pravilen
# to naredimo z uporabo else stavka, ki sledi if stavku
if a > b:
    print("a je večji od b")
else:
    print("a NI večji od b")
# if stavke lahko tudi združimo z else stavki
# to naredimo z elif stavkom, ki se izvede tako kot else stavek, ampak samo če je še njegov pogoj pravilen
if a > b:
    print("a je večji od b")
elif a < b:
    print("b je večji od a")
else:
    print("a in b sta enaka")


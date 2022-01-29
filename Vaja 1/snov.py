# PODATKOVNI TIPI IN VNOS UPORABNIKA
# Kako narediti svoje programe bolj uporabne

# PRETVARJANJE PODATKOVNIH TIPOV
# Vrste podatkovnih tipov:
# - int     - cela števila
# - str  - besedilo
# - float   - decimalna števila
# - bool    - logični tip(True/False)
celo_stevilo = 5
besedilo = "To je besedilo"
decimalno_stevilo = 1.2
logicni_tip = True

# Podatkovne tipe pretvarjamo med sabo z uporabo zgornjih funkcij
a = str(50)
print(a * 3)  # 505050
b = int("50")
print(b * 3)  # 150
c = float("1.2")
print(c * 3)  # 3.6
d = bool(0)
print(d)  # False

# - str pretvarja karkoli dobesedno v besedilo, tako kot nam je bil podatek prikazan
#   10 -> "10"; 1.2 -> "1.2"; True -> "True"
# - int pretvori vse v celo številko, če to lahko naredi:
#   1.2 -> 1; "10" -> 10; True -> 1; "deset" -> error;
# - float pretvori vse v decimalno številko, če to lahko naredi:
#   1 -> 1.0; "1.2" -> 1.2; False -> 0.0; "ena cela dva" -> error;
# - bool pretvarja karkoli in poskuša stvar vmestiti v pravilni logični razred(True/False)
#   0 -> False; 0.2 -> True; "besedilo" -> True; "" -> False
#   int -> bool (0 == False, karkoli drugega == True)
#   float -> bool (0.0 == False, karkoli drugega == True)
#   str -> bool ("" == False, karkoli drugega == True)

# Tako lahko naredimo takšne čudne izraze
e = 1.2
e = bool(int(float(str(e))))
print(e)  # True

# IF STAVKI IN PODATKOVNI TIPI
# if stavek vedno pretvori vsak pogoj v podatkovni tip bool, saj se s tem izogne nepotrebnim napak
# zaradi tega lahko v if stavke kot pogoje vsavljamo cela števila, decimalna števila ali celo besedila
# vse to namesto logičnih pogojev
a = -1
if a:
    print("število ni nič")
else:
    print("število je nič")
a = 0
if a:
    print("število ni nič")
else:
    print("število je nič")
a = "besedilo"
if a:
    print("besedilo ni prazno")
else:
    print("besedilo je prazno")
a = ""
if a:
    print("besedilo ni prazno")
else:
    print("besedilo je prazno")

# VNOS UPORABNIKA
# Če želimo izkoristiti ves potencial naših programov, moramo uporabniku dovoliti, da s programom komunicira.
# Za vnos podatkov uporabimo funkcijo input().
# Ta funkcija čaka, da uporabnik vpiše željeni podatek v konzolo, ki ga nato lahko naš program uporabi.
ime = input("Kako ti je ime? ")
starost = input("Koliko si star/a? ")
print("Pozdravljen/a " + ime + ", star/a " + starost + " let!")
# Računanje z vnešenimi podatki
# Funkcija input vedno vrne podatek v obliki besedila(str), kar pomeni, da ne moremo z njim računati, kot z ostalimi števili
# Če hočemo podatek uporabiti, kot kaj drugega kot besedilo, ga moramo pretvoriti
ime = input("Kako ti je ime? ")
starost = int(input("Koliko si star/a? "))
print("Pozdravljen/a " + ime + ", rojen/a leta " + str(2022 - starost) + "!")


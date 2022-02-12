# ZANKE (WHILE - DOKLER)
# Včasih si želimo naše dele kode večkrat izvajati. Tukaj pridejo na vrsto zanke.
# Zanke so neki stavki, ki nam omogočijo, da se določeni deli naše kode večkrat ponovijo pod nekim pogojem.
# Tako kot nam IF stavki omogočajo, da poženemo samo določen del kode, nam naše zanke omogočijo del kode pognati večkrat
# Našo zanko napovemo z besedo "while", kateri sledi pogoj. Isto kot IF stavek.
# In ta zanka se bo izvajala, dokler je pogoj v zanki izpolnjen.

# Primer zanke, ki se nikoli ne izvede
while False:
    print("ta zanka se nikoli ne izvede")

# Primer zanke, ki se izvaja v neskončnost
while True:
    print("ta zanka se ne neha izvajati")

# Zanka, ki se izvede 10x
stetje = 1
while stetje <= 10:
    print("ta zanka se je izvedla " + str(stetje) + "-krat")
    stetje += 1  # to je isto, kot če bi naredili: stetje = stetje + 1 (prišteje 1)

# Zanka, ki se izvaja, dokler ne vpišemo 0
vnos = 1
while vnos:
    vnos = int(input("Vnesi celo številko: (0, če želiš zaključiti): "))

# Zdaj vidimo, da lahko zanke izvajamo poljubno-krat želimo.
# Lahko nikoli, za vedno. Lahko za določeno število-krat, lahko za nedoločeno število-krat

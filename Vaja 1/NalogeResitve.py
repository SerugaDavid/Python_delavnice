print("Naloga 1")
besedilo = input("Vnesi besedilo: ")
if besedilo:
    print(besedilo)
else:
    print("Uporabnik ni vnesel besedila!")

print("\nNaloga 2")
prijatelji = int(input("Koliko prijateljev ima Muri?: "))
if prijatelji:
    print("Vsakemu prijatelju daj: " + str(10/prijatelji) + "€")
else:
    print("Muri, obdrži svojih 10€!")

povprecje = float(input("Kakšno imaš povprečje?: "))
if povprecje < 1.5:
    print("Nezadostno")
elif povprecje < 2.5:
    print("zadostno")
elif povprecje < 3.5:
    print("dobro")
elif povprecje < 4.5:
    print("prav dobro")
elif povprecje <= 5:
    print("odlično")
else:
    print("napačno povprečje")

print("\nNaloga 4")
a = int(input("Dolžina stranice a: "))
st_kamenckov = 4 * (a - 1)  # st_kamenckov = a * 2 + 2 * (a - 2)
if st_kamenckov:
    print(st_kamenckov)
else:
    print(1)

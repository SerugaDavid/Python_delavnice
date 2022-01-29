## Naloge za prve vaje

### Naloga 1
Uporabnika prosi naj vnese besedilo v konzolo in nato 
to besedilo izpiši. Če pa je uporabnik pustil vnos prazen,
pa izpiši: `Uporabnik ni vnesel besedila!`

Primer:
```
> Vnesi besedilo: Danes je lep dan!
> Danes je lep dan!

> Vnesi besedilo: 
> Uporabnik ni vnesel besedila!
```

### Naloga 2
Maček Muri ima 10€ in bi jih razdelil med svoj prijatelje. 
Povejte mu koliko prijateljev ima in nato izračunajte koliko
mora vsakemu od njih dati. Ne pozabite, da če Muri nima
prijateljev, teh 10€ ne bo mogel razdeliti. V tem primeru
izpišite: `Muri, obdrži svojih 10€!`

Primer:
```
> Koliko prijateljev ima Muri?: 3
> Vsakemu prijatelju daj: 3.3333333333333335€

> Koliko prijateljev ima Muri?: 0
> Muri, obdrži svojih 10€!
```

### Naloga 3
Janezka zanima kakšen uspeh bo mel na koncu leta pri
matematiki, glede na povprečje njegovih trenutnih ocen.
```
 < 1.5 = nezadostno
 < 2.5 = zadostno
 < 3.5 = dobro
 < 4.5 = prav dobro
>= 4.5 = odlično
```
Vprašaj Janezka po njegovem povprečju in mu povej njegov
uspeh.

Primer:
```
> Kakšno imaš povprečje?: 3.76
> prav dobro

> Kakšno imaš povprečje?: 4.49
> prav dobro

> Kakšno imaš povprečje?: 4.5
> odlično
```

### Naloga 4
Na tla želite položiti kamenčke v obliki kvadrata z neko
dolžino stranice `a`, ki jo bo uporabnik vnesel v program.
Program naj izračuna koliko kamenčkov potrebujemo, da z njimi
zgradimo kvadrat z dolžino stranice `a`
```
a = 1
*
1 kamenček

a = 2
* *
* *
4 kamenčki

a = 5
* * * * *
*       *
*       *
*       *
* * * * *
16 kamenčkov
```

Primer:
```
> Dolžina stranice a: 1
> 1

> Dolžina stranice a: 2
> 4

> Dolžina stranice a: 3
> 8

> Dolžina stranice a: 4
> 12

> Dolžina stranice a: 5
> 16

> Dolžina stranice a: 6
> 20
```

### Domača naloga
Napišite program, ki bo lahko računal ploščine različnih
likov, kot so: kvadrat, pravokotnik, krog in trikotnik.

Program naj vas vpraša, za kateri lik bi računali ploščino
in na podlagi odgovora vas vpraša po željenih podatkih
za izračun. Če bo uporabnik vnesel nepričakovano številko
lika naj mu program izpiše: `Napačna izbira!`

Primer:
```
> Izberi vrsto kalkulatorja:
Ploščina kvadrata (0)
Ploščina pravokotnika (1)
Ploščina kroga (2)
Ploščina trikotnika (3): 0
> Vnesi stranico a: 5
> 25

> Izberi vrsto kalkulatorja:
Ploščina kvadrata (0)
Ploščina pravokotnika (1)
Ploščina kroga (2)
Ploščina trikotnika (3): 1
> Vnesi stranico a: 3
> Vnesi stranico b: 4
> 12

> Izberi vrsto kalkulatorja:
Ploščina kvadrata (0)
Ploščina pravokotnika (1)
Ploščina kroga (2)
Ploščina trikotnika (3): 2
> Vnesi polmer: 6
> 113.04

> Izberi vrsto kalkulatorja:
Ploščina kvadrata (0)
Ploščina pravokotnika (1)
Ploščina kroga (2)
Ploščina trikotnika (3): 3
> Vnesi stranico a: 3
> Vnesi višino na a: 7
> 10.5

> Izberi vrsto kalkulatorja:
Ploščina kvadrata (0)
Ploščina pravokotnika (1)
Ploščina kroga (2)
Ploščina trikotnika (3): 4
> Napačna izbira!
```
## Naloge za druge vaje

### Naloga 1
Napiši program, ki prejme celo številko in nato prešteje do
vključno tiste številke.

Primer:
```
> Vnesi številko: 13
1
2
3
4
5
6
7
8
9
10
11
12
13
```

### Naloga 2
Janezek je bil spet preglasen pri pouku in mu je zaradi tega
učiteljica rekla naj napiše "Pri pouku bom tiho" 10x. Ampak
Janezek bi rad imel program, ki bi napisal karkoli, kolikokrat
bi on to želel. Pomagaj Janezku napisati tak program.

Primer:
```
> Vnesi beseilo, ki ga želiš ponavljati: Pri pouku bom tiho
> Vnesi kolikokrat želiš besedilo ponoviti: 7
Pri pouku bom tiho
Pri pouku bom tiho
Pri pouku bom tiho
Pri pouku bom tiho
Pri pouku bom tiho
Pri pouku bom tiho
Pri pouku bom tiho
```
Če se dobro spomnite ure, ko ste se učili dela z besedilom,
lahko to nalogo rešite tudi brez zanke.

### Naloga 3
Napišimo program, ki bo sešteval številke, dokler ne vnesemo 0.
Potem, naj izpiše njihov seštevek.

Primer:
```
> Vnesi številko: 15.6
> Vnesi številko: 734
> Vnesi številko: 23.11343
> Vnesi številko: 9.8
> Vnesi številko: 3.14
> Vnesi številko: 1.41
> Vnesi številko: 0
Seštevek je: 787.0634299999999
```

### Naloga 4
Napišimo program, ki bo shranil besedilo, ki ga napišemo po
vrsticah. Če je vrstica prazna, naj program besedilo izpiše.
Program je zelo podoben tistemu zgoraj.
```
> Vnesi vrstico: mijav
> Vnesi vrstico: hov
> Vnesi vrstico: ne ne grem domov
> Vnesi vrstico: hov
> Vnesi vrstico: mijav
> Vnesi vrstico: 
mijav
hov
ne ne grem domov
hov
mijav

```

## Domača naloga
Napisali bomo kratek programček, ki se imenuje "3n + 1". 
Ta deluje tako, da v naš program vnesemo eno številko in
potem jo ta preveri in če je deljiva z 2 jo deli z 2, če pa ni
potem pa jo pomnoži s 3 in prišteje 1, in to ponavljamo, dokler
ne pridemo na število 1. 

Če imamo začetno številko 11, ta simulacija izgleda tako:
```
11  // ni delijivo z 2
34  // delijivo z 2
17  // ni delijivo z 2
52  // delijivo z 2
26  // delijivo z 2
13  // ni delijivo z 2
40  // delijivo z 2
20  // delijivo z 2
10  // delijivo z 2
5   // ni delijivo z 2
16  // delijivo z 2
8   // delijivo z 2
4   // delijivo z 2
2   // delijivo z 2
1   // delijivo z 2
```

Primer programa pa izgleda takole:
```
> Vnesi začetno številko: 11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
```
Za vse tiste, ki si želite še kak dodatek, napišite program,
tako da izpiše še kolikokrat se je zanka izvedla. 
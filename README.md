# A the-internet-herokuapp.com oldal UI és teljesítmény tesztjeit látod itt.
## UI tesztek:
### Broken Image
Ezzel a feladattal azt lehet gyakorolni, hogy megtaláljuk azokat a képeket
amik nem töltődtek be. Azt a megoldást választottam, hogy egy ciklussal végig
megyek a DOM elemeken. Azt vizsgálom, hogy a valós szélessége a képnek nagyobb
legyen 0 pixelnél.  
Mivel tudjuk, hogy az oldalon van kettő kép ami nem töltődik be ezért a tesztet
expected failure-ként írtam meg, így nem lesz failed. Ez azért jó mert a 
tesztcsomag nem fog elbukni és nem küld a CI/CD rendszer feleslegesen üzenetet.
### Dynamic Loaded
Ezen az oldalon két irányba is tudunk tesztelni.

* Example 1: Az elem ott van a DOM-ban, de rejtett (display: none).
* Example 2: Az elem egyáltalán nem létezik a DOM-ban, 
amíg rá nem kattintasz a start gombra.

Mivel PlayWrightot használok ezért egy teszttel mind a két oldalt tudom tesztelni.
A PlayWright locator akkor fut le amikor már ott van az elem.
Az expect automatikus 5s vár viszont ezen az oldalon ha nem növeljük a timeoutot
akkor a tesztünk elbukik. A tesztnél elsőnek azt vizsgálom, hogy megjelent-e a 
felirat, a második ellenőrzés pedig a szöveg tartalmára vonatkozik.
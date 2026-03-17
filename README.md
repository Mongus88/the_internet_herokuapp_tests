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
### From Authentication
Egy egyszerű login tesztelést tudunk ezen az oldalon csinálni. A tesztemben én a
hibás felhasználó és jelszó megadást próbáltam. Az oldalon egyébként szerepel
érvényes bejelentkezési adatok is így a logout-ot is tudjuk ellenőrizni. A mezőket
egyszerű megtalálni semmi trükk nics az oldalon. Elősnek azt vizsgálom, hogy megjelenik-e
az error elem. A következő teszt azt vizsgálja helyes-e a felirat ami ilyenkor feljön.
A harmadik teszt meg egy CSS verification ami a dizájnra vonatkozik.
### Javascript Alerts
Az ilyen rendszerszintű ablakokkal az a gond, hogy nem része a DOM fának.
Mivel nem része a HTML-nek ezért a locatorral nem tudunk rátalálni a gombokra, mezőkre.
A PlayWright esemény kezelőjét (on, once) használom ami figyeli a böngészőt, hogy van-e
esemény (dialog) amit a böngésző küld. A tesztek vizsgálják azt, hogy a felugró
ablakban mi a felirat, és az interakció után az eltünt ablka után mi lett az eredmény.
### Challenging Dom
Dinamikusan változó elemekkel tudunk teszteket készíteni ezen az oldalon.
Bármelyik gombot nyomjuk meg akkor az elmek változnak, kivéve a poziciójuk.
Mivel a HTML kódból kiderül, hogy egy konténerben vannak egymás allatt, így az
indexelést választottam.
* Első tesztben azt nézzük meg, hogy a kék gomb megnyomása után változik-e a számsor.
Ez azért trükkös mert a számsor Canvas frissül. A számso értékét egy Monkey Patch-el
oldottam meg. Fontos, hogy a figyelést már az oldal eléjén el kell kezdeni és a gombnyomás
előtt egy változóba rögzíteni kell az értéket. Eztután kattintunk, az oldla frissül
a figyelő elkapja a számot és mentjük egy új változóba. Ezután hasonlítjuk össze a két
változót. Lehetett volna screanshotokat készíteni, a canva kép pixel számát összevetni vagy
OCR programot használni pl.: Tessaract
* A második tesztben a piros gomb ID frissülését nézzük meg. Itt semmi különös nincs
oldalbetöltése után lekérjük az ID-t amit a kattintás utáni ID-val vetünk össze.
* A harmadik tesztnél a zöld gomb CSS osztáláyt ellenőrizzük, hasonló mint a második
tesz csak itt nem kell kattintani. Az oldal betöltése után már ellenőrizhetjük az class
nevét.
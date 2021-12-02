# Raspberry Pi Pico Bird Shooter

Lekcja jest częścią pełnego kursu, który został przygotowany dla szkół: Akademia Nauki i Rozowoju w Żorach oraz EMT Kids w Gliwicach, gdzie można wziąć udział w pełnym szkoleniu. Kurs jest przystosowany dla dzieci i młodzieży w wieku od 12 do 14 lat. Ze względu na przeznaczenie kursu, programy częściowo zostały napisne w języku polskim.

## Pełny program – kolejne zajęcia
![](img/Obraz1.gif)

# Program testowy – plan na dzisiaj
![](img/Obraz2.gif)

## Założenia projektu

Gra polegająca na zestrzeliwaniu przelatujących ptaków\. Przez dwie kolejne lekcje będziemy tworzyć grę sterowaną poprzez żyroskop podłączony do Raspberry Pi Pico\. Żyroskop będzie wykorzystany do ustawienia celownika na ekranie\, który pozwoli nam na zestrzelenie przelatujących ptaków\. Potrzebny układ elektroniczny nie jest skomplikowany\, ale będziemy musieli zbudować go ponownie na następnych zajęciach\.



## Schemat projektu

![](img/Obraz3.png)

# Pico

Dokładamy kolejny przycisk\, którego wartości wypisujemy w porcie szeregowym\.
Ten przycisk posłuży nam jako spust do wykorzystania w grze\.

```
while True:
    katy = zmierz_kat(skalibrowane, 2)
 
    if nowa_kalibracja.value():
        offset_x=katy['GyX']
        offset_y=katy['GyY']
        offset_z=katy['GyZ']
    
    print("%.2f,%.2f,%.2f" % (katy['GyX']-offset_x,
                              katy['GyY']-offset_y,
                              katy['GyZ']-offset_z))
```

## PC - Biblioteki do podpięcia

```
import serial
from serial import Serial
import pygame
import time
from pygame.locals import *
import random
```


## PC funkcja cz. 1

Pobieramy dane z Pico i wykorzystujemy je do obliczenie pozycji wskaźnika\. Dodatkowo możemy wyświetlić dane w konsoli\, żeby sprawdzić ich poprawność\. Dla ciekawskich można sprawdzić co oznaczają nazwyroll\,pitchiyaw\.

```
def render_celownika():
    global odczyty, ostatni_przycisk

    odczyty+=1
    dane = pico.readline()

    if dane:
        dane = dane.decode()
        dane = dane.split(',')

        #Obrót wokół osi Z
        yaw = float(dane[2])
        #obrót wokół osi X
        pitch = float(dane[0])
        #Przycisk spustu
        przycisk = int(dane[3])

        #print("%.2f, %.2f" %(yaw, pitch))

        #Obliczamy pozycję wskaźnika na podstawie odebranych kątów
        x = szerokosc_okna/2 * (1 - yaw/20)
        y = wysokosc_okna/2 * (1 + pitch/20)
```

## Dalsza część funkcji rysującej wskaźnik

Dbamy o to\, żeby wskaźnik nie wyszedł poza okno\. Dodatkowo wprowadzamy warunek\, który czyści port szeregowy czas co jakiś czas\. Jak się okazuje\, zbyt duża nieodczytanych danych może spowodować spowolnione działanie\.

```
        #Jeżli pozycja wskaźnika będzie poza ekranem to go blokujemy
        if x > szerokosc_okna - 20: x = szerokosc_okna - 10
        if x < 0: x = 0

        if y > wysokosc_okna - 20: y = wysokosc_okna - 10
        if y < 0: y = 0

        #Po 200 odczytach czyścimy port szeregowy 
        if odczyty==200:
            odczyty=0
            #Czyszczenie portu 
            pico.flushInput()
            for i in range(5):
                dane=pico.readline()

        #Rysjemy wskaźnik
        do_narysowania = pygame.draw.rect(okno, pygame.Color(0,0,0),(x, y, 10, 10))
        pygame.display.update(do_narysowania)
```

## PC pętla główna

Inicjujemy połączenie z Pico oraz tworzymy odpowiednie zmienne\. Opcja __DOUBLEBUF__ pozwoli na szybsze działanie programu\.

```
#Tworzymy połączenie z portem szeregowym 
pico = serial.Serial(port = "COM3", baudrate=9600)

#Tworzymy grę w pygame
szerokosc_okna = 1200
wysokosc_okna = 800
pygame.init()
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna), DOUBLEBUF)

#Zmienne globalne
odczyty=0
ostatni_przycisk=0

#GŁÓWNA PĘTLA
run=True
while run:
    okno.fill(pygame.Color(0,0,255))
    render_celownika()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                    
    pygame.display.update()
```

## Koniec!


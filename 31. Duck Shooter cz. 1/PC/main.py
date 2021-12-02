import serial
from serial import Serial
import pygame
import time
from pygame.locals import *
import random

#funkcja rysująca wskaźnik/celownik
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

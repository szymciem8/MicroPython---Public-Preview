from machine import I2C, Pin
import mpu6050
import math
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
gyro = mpu6050.accel(i2c)

nowa_kalibracja = Pin(2, Pin.IN, Pin.PULL_DOWN)

katy = {'GyX':0, 'GyY':0, 'GyZ':0}

def srednia_wartosc(n=5):
    srednie = {'GyX':0, 'GyY':0, 'GyZ':0}
    for i in range(n):
        for klucz in srednie:
            srednie[klucz] += gyro.get_values()[klucz]/n
        
    return srednie

#Funkcja kalibrująca pozwala na określenie dryfu żyroskopu
#Dzięku czemu dostajemy dokładniejszy pomiar
def kalibracja(granica=100, n=100):
    skalibrowane = {'GyX':0, 'GyY':0, 'GyZ':0}
    for klucz in skalibrowane:
        for i in range(n):
            while True:
                val1 = gyro.get_values()[klucz]
                val2 = gyro.get_values()[klucz]
                if abs(val1-val2) < granica:
                    break
            
            skalibrowane[klucz] += val1/n 

    return skalibrowane

#Kąt uzyskujemy poprzez sumowanie szybkości kątowych
#Można to zrobić dokłdniej
def zmierz_kat(skalibrowane, n=5):
    kat_sredni = srednia_wartosc(n)
    for klucz in katy:
        kat_sredni[klucz] -= skalibrowane[klucz]
        if kat_sredni[klucz] > 0:
            kat_sredni[klucz] = math.floor(kat_sredni[klucz])
        elif kat_sredni[klucz] < 0:
            kat_sredni[klucz] = math.ceil(kat_sredni[klucz])
        katy[klucz] += kat_sredni[klucz]*0.0000611*n
        
    return katy
    
skalibrowane = kalibracja()

offset_x=0
offset_y=0
offset_z=0

while True:
    katy = zmierz_kat(skalibrowane, 2)
 
    #Pomimo kalibracji co jakiś czas należy skalibrować
    #żyroskop na nowo okrzystając z przycisku
    #Kalibracja polega na pobraniu zdryfowanej pozycji i odjęciu
    #jej od nowych pomiarów
    if nowa_kalibracja.value():
        offset_x=katy['GyX']
        offset_y=katy['GyY']
        offset_z=katy['GyZ']
    
    print("%.2f,%.2f,%.2f" % (katy['GyX']-offset_x,
                              katy['GyY']-offset_y,
                              katy['GyZ']-offset_z))
    
    
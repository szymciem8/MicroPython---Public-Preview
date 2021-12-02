![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice0.png)

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice1.png)

# Raspberry Pi Pico Bird Shooter

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice2.png)

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice3.png)

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice4.png)

# Pełny program – kolejne zajęcia

# Program testowy – plan na dzisiaj

# Założenia projektu

Gra polegająca na zestrzeliwaniuprzelatujących ptaków\.

Przez dwie kolejne lekcje będziemy tworzyć grę sterowaną poprzez żyroskop podłączony do Pico\.

Żyroskop będzie wykorzystany do ustawienia celownika na ekranie\, który pozwoli nam na zestrzelenie przelatujących ptaków\.

Potrzebny układ elektroniczny nie jest skomplikowany\, ale będziemy musieli zbudować go ponownie na następnych zajęciach\.

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice5.png)

# Schemat projektu

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice6.png)

# Pico

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice7.png)

Dokładamy kolejny przycisk\, którego wartości wypisujemy w porcie szeregowym\.

Ten przycisk posłuży nam jako spust do wykorzystania w grze\.

# PC - Biblioteki do podpięcia

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice8.png)

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice9.png)

# PC funkcja cz. 1

Pobieramy dane z Pico i wykorzystujemy je do obliczenie pozycji wskaźnika\.

Dodatkowo możemy wyświetlić dane w konsoli\, żeby sprawdzić ich poprawność\.

Dla ciekawskich można sprawdzić co oznaczają nazwyroll\,pitchiyaw\.

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice10.png)

Dalsza część funkcji rysującej wskaźnik

Dbamy o to\, żeby wskaźnik nie wyszedł poza okno\.

Dodatkowo wprowadzamy warunek\, który czyści port szeregowy czas co jakiś czas\. Jak się okazuje\, zbyt duża nieodczytanych danych może spowodować spowolnione działanie\.

# PC pętla główna

![](img/Duck%20Shooter%20cz%201%20%E2%80%94%20Gliwice11.png)

Inicjujemy połączenie z Pico oraz tworzymy odpowiednie zmienne\.

Opcja __DOUBLEBUF__ pozwoli na szybsze działanie programu\.

# Koniec!


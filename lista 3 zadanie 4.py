import qrcode
import cv2

def zakoduj_w_qr(wiadomosc, ścieżka_docelowa):

    """Stworzenie kodu QR dla podanej wiadomości.
    
    Input:
    wiadomosc(str) - dane, dla których zostanie wygenerowany kod qr.
    ścieżka_docelowa - ścieżka, pod którą zostanie zapisany wygenerowany kod qr.
    """
    kod = qrcode.make(wiadomosc)
    kod.save(ścieżka_docelowa)

def odkoduj_qr(ścieżka_docelowa):

    """Odkodowanie stworzonego kodu QR.
    
    Input:
    ścieżka_docelowa - ścieżka, pod którą został zapisany kod qr.
    Output:
    Zwrócenie oryginalnej wiadomości.
    """
    reprezentacja_kodu = cv2.imread(ścieżka_docelowa)
    odkodowanie = cv2.QRCodeDetector()
    oryginalna_wiadomosc, wartości, macierze = odkodowanie.detectAndDecode(reprezentacja_kodu)
    return(oryginalna_wiadomosc)

wiadomosc = "Wygeneruj kod QR"
ścieżka_docelowa = r'C:\Users\magda\Desktop\kod_qr.png'

zakoduj_w_qr(wiadomosc, ścieżka_docelowa)
print(odkoduj_qr(ścieżka_docelowa))
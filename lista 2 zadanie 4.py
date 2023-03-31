from PyPDF2 import PdfWriter, PdfReader
import os

def podział(ścieżka_do_pdf, ścieżka_docelowa, podział_stron):

    """Podziel podany plik pdf na mniejsze pliki pdf o podanych stronach i zapisz je pod wskazanymi ścieżkami.
    
    Input:
    ścieżka_do_pdf - ścieżka, pod którą znajduje się plik do podzielenia.
    ścieżka_docelowa - ścieżka, pod którą zostaną zapisane podzielone pliki pdf.
    podział_stron(list) - lista krotek, wskazująca, które strony mają się znaleźć w każdym z mniejszych pdf-ów.

    Output:
    Informacja o zapisaniu podzielonych pdf-ów.
    """

    for i in range(len(podział_stron)):
        if type(podział_stron[i]) != tuple:
            raise TypeError ("Należy podać zakres stron w formie dwuelementowej krotki!")

    rozdzielona_ścieżka_docelowa = os.path.split(ścieżka_docelowa)
    rozdzielona_ścieżka_do_pdf = os.path.split(ścieżka_do_pdf)
    if type(podział_stron) == list:
        wejsciowy_pdf = PdfReader(open(ścieżka_do_pdf, "rb"))
        for i in range(len(podział_stron)):
            wyjsciowy_pdf = PdfWriter()
            a = podział_stron[i]
            if a[1] < a[0]:
                raise ValueError ("Nie można stworzyć pdf-a w zakresie, gdzie druga liczba jest mniejsza niż pierwsza!")
            for j in range(a[0]-1, a[1]):
                wyjsciowy_pdf.add_page(wejsciowy_pdf.pages[j])
            with open(rozdzielona_ścieżka_docelowa[0]+ "\\" + "strony" + str(a[0]) + "-" + str(a[1]) + "_" + rozdzielona_ścieżka_do_pdf[1] , "wb") as plik:
                wyjsciowy_pdf.write(plik)
    else:
        raise TypeError ("Wpisz strony, na które należy podzielić plik pdf, w formie listy!")
    
    return "Podzielone pliki znajdują się pod wskazaną ścieżką."

a = r'C:\Users\magda\Desktop\wykład_piąty.pdf'
b = r'C:\Users\magda\Desktop\\'
c = [(1, 5), (6, 8), (9, 14)]

print(podział(a, b, c))

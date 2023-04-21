from PyPDF2 import PdfReader, PdfMerger

def łączenie(ścieżka_do_pdfów, ścieżka_docelowa):

    """Połącz kilka pdf-ów podanych w formie listy w jeden duży pdf.
    
    Input:
    ścieżka_do_pdf-ów(list) - lista ścieżek, pod którymi znajdują się pdf-y przeznaczone do połączenia w jeden dokument.
    ścieżka_docelowa - ścieżka, pod którą ma zostać zapisany utworzony pdf.
    """

    if type(ścieżka_do_pdfów) != list:
        return "Podaj w formie listy dokumenty, które mają zostać połączone w jeden pdf."
    
    łączenie  = PdfMerger()
    
    for pdf in ścieżka_do_pdfów:
        wejsciowy_pdf = open(pdf, "rb")
        wczytanie_pdf = PdfReader(wejsciowy_pdf)
        łączenie.append(wczytanie_pdf)
        wejsciowy_pdf.close()
    
    łączenie.write(ścieżka_docelowa)
    
    

ścieżka_do_pdfów = [r'C:\Users\magda\Desktop\strony1-5_wykład_piąty.pdf', r'C:\Users\magda\Desktop\strony6-8_wykład_piąty.pdf', r'C:\Users\magda\Desktop\strony9-14_wykład_piąty.pdf']
ścieżka_docelowa = r'C:\Users\magda\Desktop\połączony_pdf.pdf'
łączenie(ścieżka_do_pdfów, ścieżka_docelowa)


def porownanie(ścieżka_docelowa, oryginalny_pdf):

    """Porównaj pdf-y ze sobą pod kątem liczby stron oraz tekstu.
    
    Input:
    ścieżka_docelowa - ścieżka do pierwszego z pdf-ów przeznaczonych do porównania.
    oryginalny_pdf - ścieżka do drugiego z pdf-ów przeznaczonych do porównania.
    Output:
    Informacja o tym, czy pdf-y są takie same, lub o tym, czym się różnią.
    """

    plik_pierwszy = open(ścieżka_docelowa, 'rb')
    wczytaj_pdf_pierwszy = PdfReader(plik_pierwszy)

    plik_drugi = open(oryginalny_pdf, 'rb')
    wczytaj_pdf_drugi = PdfReader(plik_drugi)

    strony_pdf_pierwszego = len(wczytaj_pdf_pierwszy.pages)
    strony_pdf_drugiego = len(wczytaj_pdf_drugi.pages)

    if strony_pdf_pierwszego == strony_pdf_drugiego:
        for strona in wczytaj_pdf_pierwszy.pages:
            strona_pdf_pierwszego = strona.extract_text()
        for page in wczytaj_pdf_drugi.pages:
            strona_pdf_drugiego = page.extract_text()
        if strona_pdf_pierwszego == strona_pdf_drugiego:
            return "Pdf-y nie różnią się tekstem ani liczbą stron. Są takie same!"
        else:
            return "Tekst w pdf-ach się nie zgadza."
    else:
        return "Pdf-y nie mają takiej samej liczby stron. Nie są takie same!"


ścieżka_docelowa = r'C:\Users\magda\Desktop\połączony_pdf.pdf'
oryginalny_pdf = r'C:\Users\magda\Desktop\wykład_piąty.pdf'

print(porownanie(ścieżka_docelowa, oryginalny_pdf))


def zmiana_formatu(plik_wejściowy, plik_wyjściowy, format_wejściowy, format_wyjściowy):

    """Zmień znaki końca linii z windowsowych na unixowe lub odwrotnie.
       
    Input:
    plik_wejściowy - plik, którego znaki końca linii zostaną zmienione.
    plik_wyjściowy - plik, w którym zostaną zapisane zmiany.
    format_wejściowy - oryginalny znak końca linii (windowsowy/unixowy).
    format_wyjściowy - znak końca linii po zmianie (windowsowy/unixowy).
    """

    with open(plik_wejściowy) as plik_wejściowy, open(plik_wyjściowy, 'w') as plik_wyjściowy:
        tekst = plik_wejściowy.read()
        tekst = tekst.replace(format_wejściowy, format_wyjściowy)
        plik_wyjściowy.write(tekst)


format_windowsowy = '\n'
format_unixowy = '\r\n'
zmiana_formatu(r'C:\Users\magda\Desktop\znaki_konca_linii.txt', r'C:\Users\magda\Desktop\plik_wyjściowy.txt', format_windowsowy, format_unixowy)


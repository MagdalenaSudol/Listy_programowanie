from PIL import Image


def wymiar(sciezka_oryginalna, rozmiary_wyjsciowe, sciezka_wyjsciowa):

    """Zwróć obraz podany jako sciezka_oryginalna, o rozmiarze podanym jako rozmiary_wyjsciowe, i zapisz go pod wskazaną ścieżką.

    Input:
    sciezka_oryginalna - ścieżka do oryginalnego pliku.
    rozmiary_wyjsciowe - rozmiary, które ma przyjąć zmieniony obraz.
    sciezka_wyjsciowa - ścieżka, pod którą ma zostać zapisany zmieniony obraz.   

    Output:
    Informacja o zapisaniu obrazu pod wskazaną ścieżką.
    """
    
    if type(rozmiary_wyjsciowe) != tuple:
        raise TypeError ("Rozmiary muszą mieć formę krotki")
    obraz = Image.open(sciezka_oryginalna)
    obraz.show()
    nowy_obraz = obraz.resize(rozmiary_wyjsciowe)
    nowy_obraz.show()
    nowy_obraz.save(sciezka_wyjsciowa)
    return "Obraz został zapisany pod wskazaną ścieżką."

sciezka_wej = r'C:\Users\magda\Desktop\brama_brandenburska.jpg'
sciezka_wyj = r'C:\Users\magda\Desktop\zmienione_zdjęcie.jpg'

a = wymiar(sciezka_wej, (900, 900), sciezka_wyj)
print(a)
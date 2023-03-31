from PIL import Image

def znak(obrazek_podstawowy, znak_wodny, ścieżka_docelowa):
    """Nałóż znak wodny na obraz.
    
    Input:
    obrazek_podstawowy - obraz, na który ma zostać naniesiony znak wodny.
    znak_wodny - grafika, która ma zostać małożona na obraz.
    ścieżka_docelowa - ścieżka, pod którą ma być zapisany obraz z naniesionym znakiem wodnym.

    Output:
    Obraz z nałożonym znakiem wodnym, zapisany pod wskazaną ścieżką.
    """

    obraz1 = Image.open(obrazek_podstawowy)
    obraz2 = Image.open(znak_wodny)
    obraz2 = obraz2.resize(obraz1.size)

    obraz1 = obraz1.convert("RGBA")
    obraz2 = obraz2.convert("RGBA")
 
    obraz1.putalpha(240)
    obraz2.putalpha(30)

    obraz_wyjściowy = Image.alpha_composite(obraz1, obraz2)
    obraz_wyjściowy.show()

    obraz_wyjściowy.save(ścieżka_docelowa)


obrazek_podstawowy = r'C:\Users\magda\Desktop\brama_brandenburska.jpg'
znak_wodny = r'C:\Users\magda\Desktop\znak_wodny.jpg'
ścieżka_docelowa = r'C:\Users\magda\Desktop\obrazek_ze_znakiem_wodnym.png'

znak(obrazek_podstawowy, znak_wodny, ścieżka_docelowa)





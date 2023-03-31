from zipfile import ZipFile
import os
import shutil
from datetime import datetime

def pliki_w_folderze(ścieżka):

    lista_plików = []

    for pliki in os.walk(ścieżka):
        for plik in pliki:
            lista_plików.append(plik)
    return lista_plików

a = r'C:\Users\magda\Desktop\programowanie zajęcia 29.03-05.04'

print(pliki_w_folderze(a))


def tworzenie_kopii_i_zip(ścieżka, ścieżka_docelowa):

    data = datetime.now()
    data_w_nazwie_pliku = data.strftime("%Y-%m-%d")

    ścieżki_plików = pliki_w_folderze(ścieżka)
    wczytane_ścieżki = ścieżki_plików[-1]

    for i in range(len(wczytane_ścieżki)):
        skopiowany_plik = open(str(data_w_nazwie_pliku) + wczytane_ścieżki[i], "w")
        shutil.copy2(ścieżka + "\\" + wczytane_ścieżki[i], ścieżka + "\\" + str(data_w_nazwie_pliku) + wczytane_ścieżki[i])
        skopiowany_plik.close()
        with ZipFile(ścieżka_docelowa, mode="a") as zip:
            zip.write(ścieżka + "\\" + str(data_w_nazwie_pliku) + wczytane_ścieżki[i])
    
    return "Pliki z podanego folderu zostały zapisane w podanym folderze zip."

a = r'C:\Users\magda\Desktop\programowanie zajęcia 29.03-05.04'
b = r'C:\Users\magda\Desktop\kopie_zapasowe.zip'

pliki_w_folderze(a)
tworzenie_kopii_i_zip(a, b)
from zipfile import ZipFile
from datetime import datetime
import os
import shutil

def kopia(ścieżka_do_pliku, ścieżka_docelowa):
    """Stwórz kopię zapasową pliku i zapisz ją w podanym folderze zip.

    Input:
    ścieżka_do_pliku - ścieżka do pliku, którego kopia ma zostać stworzona.
    ścieżka_docelowa - ścieżka, pod którą ma zostać zapisana kopia pliku.
    """
    data = datetime.now()
    data_w_nazwie_pliku = data.strftime("%Y-%m-%d")
    if type(ścieżka_do_pliku) == list:
        for i in range(len(ścieżka_do_pliku)):
            rozdzielona_ścieżka = os.path.split(ścieżka_do_pliku[i]) 
            skopiowany_plik = open(str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1], "w")
            shutil.copyfile(ścieżka_do_pliku[i], rozdzielona_ścieżka[0] + "\\" + str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1])
            skopiowany_plik.close()
            with ZipFile(ścieżka_docelowa, mode="a") as zip:
                zip.write(rozdzielona_ścieżka[0] + "\\" + str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1])
             
    elif type(ścieżka_do_pliku) == str:
            rozdzielona_ścieżka = os.path.split(ścieżka_do_pliku)
            print(rozdzielona_ścieżka[0]+ "\\" + str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1])
            skopiowany_plik = open(str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1], "w")
            shutil.copyfile(ścieżka_do_pliku, rozdzielona_ścieżka[0]+ "\\" + str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1])
            skopiowany_plik.close()
            with ZipFile(ścieżka_docelowa, mode="a") as zip:
                zip.write(rozdzielona_ścieżka[0]+ "\\" + str(data_w_nazwie_pliku) + rozdzielona_ścieżka[1])

    else:
         raise TypeError ("Wpisz pojedynczy plik lub listę plików")


a = r'C:\Users\magda\Desktop\znak_wodny.jpg'
b = r'C:\Users\magda\Desktop\kopie_zapasowe.zip'

kopia(a, b)


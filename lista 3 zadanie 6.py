import requests
from bs4 import BeautifulSoup
import webbrowser

def losuj_artykuł():

    """Wylosuj dowolny artykuł ze strony wikipedia.org i wyświetl go w przeglądarce lub wylosuj nowy, w zależności od decyzji użytkownika.
    
    Input:
    T/N - decyzja użytkownika na temat dalszego działania programu (wyświetl stronę - "T" lub wylosuj kolejny artykuł - "N").
    Output:
    Wyświetlenie strony internetowej.
    """

    print("Jeżeli wylosowany artykuł ci się podoba, wpisz T. Jeżeli nie, wpisz N.")
    proba = 1
    while proba <= 5:
        strona_internetowa = 'https://en.wikipedia.org/wiki/Special:Random'
        pobranie_strony = requests.get(strona_internetowa)
        zmiana = BeautifulSoup(pobranie_strony.text, 'html.parser')
        tytuł = zmiana.select("#firstHeading")[0].text
        print(tytuł)
        pytanie = input("Czy wyświetlić ten artykuł?")
        if str(pytanie) == "T":
            webbrowser.open('https://en.wikipedia.org/wiki/' + tytuł)
            break
        elif str(pytanie) == "N":
            proba += 1 
        else:
            raise ValueError ("Podany znak nie jest literą T ani N. Kończę działanie!")
        
losuj_artykuł()
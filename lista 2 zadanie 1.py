import random
import string

def haslo(liczba_znakow, rodzaj_znakow = [string.ascii_letters, string.digits, string.punctuation]):
    """Wygeneruj losowe hasło o podanej liczbie i rodzaju znaków.

    Input:
    liczba_znakow(int) - liczba znaków hasła.
    rodzaj_znakow(list) - wszystkie znaki, które mogą posłużyć do wygenerowania hasła.
    
    Output:
    ciag_znakow(str) - wygenerowane hasło.
    """
    if type(liczba_znakow) == str or type(liczba_znakow) == float:
        raise ValueError ("Podaj całkowitą liczbę znaków, z których ma być zbudowane hasło!")
    
    if type(rodzaj_znakow) != list:
        raise TypeError ("Podaj wszystkie znaki, które mogą posłużyć do wygenerowania hasła, w formie listy!")
    
    lista = []
    for i in range(len(rodzaj_znakow)):
        lista.extend(rodzaj_znakow[i])

    haslo = []
    for i in range(liczba_znakow):
        haslo.append(lista[random.randint(0,(len(lista)-1))])

    ciag_znakow = ""
    for i in range(len(haslo)):
        ciag_znakow = ciag_znakow + haslo[i]

    return ciag_znakow

print(haslo(8))


import string

def działanie(ciąg_znaków):

    """Stwórz słupek dla podanego działania. Możliwe działania: dodawanie, odejmowanie, mnożenie.

    Input:
    ciąg_znaków(str) - działanie, dla którego ma zostać wygenerowany słupek.
    Output:
    Słupek wygenerowany dla podanego działania wraz z wynikiem.
    """
    lista_liczb_1 = list((str(ciąg_znaków)).split(" "))


    if "+" in ciąg_znaków:
        for i in range(len(lista_liczb_1)):
            while "+" in lista_liczb_1:
                lista_liczb_1.remove("+")

        for i in range(len(lista_liczb_1)-1):
            print(lista_liczb_1[i].rjust(10))

        print("+", lista_liczb_1[i+1].rjust(8))
        wynik = 0
        for i in range(len(lista_liczb_1)):
            liczba = int(lista_liczb_1[i])
            wynik += liczba
    elif "-" in ciąg_znaków:
        for i in range(len(lista_liczb_1)):
            while "-" in lista_liczb_1:
                lista_liczb_1.remove("-")

        for i in range(len(lista_liczb_1)-1):
            print(lista_liczb_1[i].rjust(10))

        print("-", lista_liczb_1[i+1].rjust(8))
        wynik = int(lista_liczb_1[0])
        for i in range(1, len(lista_liczb_1)):
            liczba = int(lista_liczb_1[i])
            wynik -= liczba


    elif "*" in ciąg_znaków:
        for i in range(len(lista_liczb_1)):
            while  "*" in lista_liczb_1:
                lista_liczb_1.remove("*")
            
        for i in range(len(lista_liczb_1)-1):
            print(lista_liczb_1[i].rjust(10))

        print("*", lista_liczb_1[len(lista_liczb_1)-1].rjust(8))

        wynik = int(lista_liczb_1[0])
        for i in range(1, len(lista_liczb_1)):
            liczba = int(lista_liczb_1[i])
            wynik_1 = wynik*liczba
            wynik = wynik_1

    wynik = str(wynik)
    print("-"*10)
    return(wynik.rjust(10))


ciąg_znaków = "135 - 30"
print(działanie(ciąg_znaków))
print(" ")

ciąg_znaków = "13 * 7 * 21"
print(działanie(ciąg_znaków))
print(" ")

ciąg_znaków = "21 + 75895 + 534"
print(działanie(ciąg_znaków))
print(" ")

ciąg_znaków = "255 + 135 + -133"
print(działanie(ciąg_znaków))

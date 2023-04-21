

def poprawnosc(dzialanie):

    """Sprawdź poprawność umieszczenia nawiasów w podanym działaniu (ich liczby, rodzajów i miejsc, w których występują).
    
    Input:
    dzialanie(str) - działanie, które ma zostać sprawdzone.
    Output:
    Informacja o poprawności umieszczenia nawiasów w działaniu.
    """

    liczba_kwadratowych_nawiasow_lewych = dzialanie.count("[")
    liczba_kwadratowych_nawiasow_prawych = dzialanie.count("]")
    liczba_okraglych_nawiasow_lewych = dzialanie.count("(")
    liczba_okraglych_nawiasow_prawych = dzialanie.count(")")
    liczba_klamrowych_nawiasow_lewych = dzialanie.count("{")
    liczba_klamrowych_nawiasow_prawych = dzialanie.count("}")
    liczba_ostrych_nawiasow_lewych = dzialanie.count("<")
    liczba_ostrych_nawiasow_prawych = dzialanie.count(">")
    if liczba_kwadratowych_nawiasow_lewych == liczba_kwadratowych_nawiasow_prawych and liczba_okraglych_nawiasow_lewych == liczba_okraglych_nawiasow_prawych and liczba_klamrowych_nawiasow_lewych == liczba_klamrowych_nawiasow_prawych and liczba_ostrych_nawiasow_lewych == liczba_ostrych_nawiasow_prawych:
        print("Liczba nawiasów się zgadza.")
    else:
        return "Sprawdź działanie. Nie zgadza się w nim liczba nawiasów."
    
    lista_znakow = list(dzialanie)
    for i in range(len(lista_znakow)-1):
        if lista_znakow[i] == lista_znakow[i+1]:
            return "Takie same nawiasy nie powinny znajdować się na sąsiednich pozycjach."
        elif lista_znakow[i] == "(" and lista_znakow[i+1] == ")" or lista_znakow[i] == "[" and lista_znakow[i+1] == "]" or lista_znakow[i] == "{" and lista_znakow[i+1] == "}" or lista_znakow[i] == "<" and lista_znakow[i+1] == ">":
            return "Postawiono puste nawiasy w działaniu."

        if "(" in lista_znakow and ")" in lista_znakow and lista_znakow.index(")") < lista_znakow.index("(") or "[" in lista_znakow and "]" in lista_znakow and lista_znakow.index("]") < lista_znakow.index("[") or "{" in lista_znakow and "}" in lista_znakow and lista_znakow.index("}") < lista_znakow.index("{") or "<" in lista_znakow and ">" in lista_znakow and lista_znakow.index(">") < lista_znakow.index("<"):
            return "Wyrażenia nie powinny zaczynać się od nawiasów prawych."

    lista_nawiasow = []
    for item in lista_znakow:
        if item == "(" or item == ")" or item == "[" or item == "]" or item == "{" or item == "}":
            lista_nawiasow.append(item)

    if ("{" in lista_nawiasow and "[" in lista_nawiasow and lista_nawiasow.index("{") > lista_nawiasow.index("[")) or ("}" in lista_nawiasow and "]" in lista_nawiasow and lista_nawiasow.index("}") < lista_nawiasow.index("]")):
        return "Zła kolejność nawiasów. Nawiasy \"{\" powinny znajdować się na zewnątrz nawiasów []."
    if ("{" in lista_nawiasow and "(" in lista_nawiasow and lista_nawiasow.index("{") > lista_nawiasow.index("(")) or ("}" in lista_nawiasow and ")" in lista_nawiasow and lista_nawiasow.index("}") < lista_nawiasow.index(")")):
        return "Zła kolejność nawiasów. Nawiasy \"{\" powinny znajdować się na zewnątrz nawiasów ()."
    if ("[" in lista_nawiasow and "(" in lista_nawiasow and lista_nawiasow.index("[") > lista_nawiasow.index("(")) or ("]" in lista_nawiasow and ")" in lista_nawiasow and lista_nawiasow.index("]") < lista_nawiasow.index(")")):
        return "Zła kolejność nawiasów. Nawiasy \"()\" powinny znajdować się na zewnątrz nawiasów []."
    if ("<" in lista_nawiasow and "(" in lista_nawiasow and lista_nawiasow.index("<") > lista_nawiasow.index("(")) or (">" in lista_nawiasow and ")" in lista_nawiasow and lista_nawiasow.index(">") < lista_nawiasow.index(")")):
        return "Zła kolejność nawiasów. Nawiasy \"<>\" powinny znajdować się na zewnątrz nawiasów ()."
    if ("<" in lista_nawiasow and "[" in lista_nawiasow and lista_nawiasow.index("<") > lista_nawiasow.index("[")) or (">" in lista_nawiasow and "]" in lista_nawiasow and lista_nawiasow.index(">") < lista_nawiasow.index("]")):
        return "Zła kolejność nawiasów. Nawiasy \"<>\" powinny znajdować się na zewnątrz nawiasów []."
    if ("<" in lista_nawiasow and "{" in lista_nawiasow and lista_nawiasow.index("<") > lista_nawiasow.index("{")) or (">" in lista_nawiasow and "}" in lista_nawiasow and lista_nawiasow.index(">") < lista_nawiasow.index("}")):
        return "Zła kolejność nawiasów. Nawiasy \"<>\" powinny znajdować się na zewnątrz nawiasów \"{\"."

        
    
przykład = "<[{(9*12)+10}]*20>"
print("Przykład 1: ")
print(poprawnosc(przykład))

przykład = "[20*20+(30]50)"
print("Przykład 2: ")
print(poprawnosc(przykład))

przykład = "<[{(9*12)+10}]*20"
print("Przykład 3: ")
print(poprawnosc(przykład))

przykład = "((12*55)-21)"
print("Przykład 4: ")
print(poprawnosc(przykład))
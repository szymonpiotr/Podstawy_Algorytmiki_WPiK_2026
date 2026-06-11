# Sortowanie

# 1a. Zdefinuj funkcję, która sortuje listę liczb - użyj rekurencji. Jeśli jest to potrzebne
# zdefiniuj funkcje pomocnicze. 
def recurSortt(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        smaller = [i for i in list[1:] if i < pivot]
        larger = [i for i in list[1:] if i >= pivot]
        return recurSortt(smaller) + [pivot]  + recurSortt(larger) 

# 1b. Zdefinuj funkcję, które sortuje listę liczb - użyj iteracji.
def iterSort(list):
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1     
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    return list  


# 2a. Zdefiniuj funkcję, która wstawi daną liczbę w odpowiednie miejsce posortowanej listy - użyj rekurencji.
def insertRec(elem,list):
    if list == []:
        return [elem]
    else: 
        if elem <= list[0]:
            return [elem] + list
        else:
            return [list[0]] + insertRec(elem,list[1:])                 

# 3a. Zdefiniuj funkcję, która sprawdzi ile razy dany element występuje na danej liście - użyj rekurencji.
def howMany(elem,list):
    if list == []:
        return 0
    else:
        if elem == list[0]:
            return 1 + howMany(elem,list[1:])
        else:
            return howMany(elem,list[1:])
            
# 3b. Zdefiniuj funkcję, która sprawdzi ile razy dany element występuje na danej liście - użyj iteracji.
def howManyIter(elem,list):
    if list == []:
        return 0
    else:
        counter = 0
        for i in list:
            if elem == i:
                counter += 1
        return counter 

# 4. Trójkąt Pacala. Zdefinuj funkcję, która dostaje dwa argumenty: numer kolumny i numer wiersza, zwraca zaś 
# liczbą Pascala która na danej współrzędnej występuje.

def pascal(wiersz, kolumna):
    if (kolumna == 0 or wiersz == kolumna):
        return 1   
    else:
        return pascal(wiersz - 1, kolumna - 1) + pascal(wiersz-1, kolumna)

# 5. Zdefiniuj funkcję "balance", która sprawdza, czy w danym Stringu nawiasy są ustawione w 
# prawidłowy sposób, tj. czy każde lewy nawias ma swój prawy nawias do pary i czy są one dobrze ustawione.



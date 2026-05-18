# Dane kontaktowe:
# Szymon Chlebowski, szymon.chlebowski@amu.edu.pl 
# Dyżury (pokój 97, budynek AB)  
# wtorek 9.00-11.00 (po uprzednim umówieniu się)

# 30 punktów: kolokwium (indywidualne przy komputerze), 
# 20 punktów: indywidualne wejściówki/wyjściówki i/lub praca w małych grupach.
 
# kod zajęć będzie dostępny na Githubie a link będzie udostepniany na stronie:
# http://sc52172.home.amu.edu.pl/

# Temat pierwszych zajęć: 
# - rozgrzewka;
# - rekurencja i iteracja: podstawy

def dodaj(liczba):
    if liczba == 0:
        return liczba
    else:
        return liczba + dodaj(liczba - 1)
    
def dodaj_ogon(liczba, temp):
      if liczba == 0:
            return temp 
      else:
            return dodaj_ogon(liczba-1, liczba+temp)   

# dodaj_ogon(3,0) = dodaj_ogon(2, 3) 
#                 = dodaj_ogon(1, 5)
#                 = dodaj_ogon(0, 6)
#                 = 6

# dodaj(3)    = 3 + dodaj(2)
#             = 3 + 2 + dodaj(1)
#             = 3 + 2 + 1 + dodaj(0)
#             = 3 + 2 + 1 + 0
#             = 6    


def dodaj_iter(liczba):
    total = 0
    for i in range(liczba+1):
        total = total+i
    return total

  
# 1a. Zdefiniuj funkcję silnia, używając standardowej rekurencji. 

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
     
# 1b. Zdefiniuj funkcję silnia, używając rekurencji ogonowej.

def factorial_tail(n,m):
    if n==0:
        return m
    else:
        return factorial_tail(n-1, n*m)
   
# 1c. Zdefiniuj funkcję silnia, używając iteracji (pętli).

def factorial_iter(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f = f*i
        return f

# 2a. Zdefiniuj funkcję zwracającą największy element w liście - wersja iteracyjna.

def maximum_iter(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max

# 2b. Zdefiniuj funkcję zwracającą największy element w liście - wersja rekurencyjna.

def maxx(lista):
      if len(lista)==1:
            return lista[0]
      else:
            reszta = lista[1:]
            if lista[0] > maxx(reszta):
                  return lista[0]
            else:
                  return maxx(reszta)  

# 3a. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja rekurencyjna.

def reverse_rec(list):
    if len(list) == 0:
        return []
    else:
        return reverse_rec(list[1:]) + [list[0]]

# reverse_rec([1,2,3])    = reverse_rec([2,3])  + [1]
#                        = (reverse_rec([3]) + [2]) + [1]
#                        = ((reverse_rec([]) + [3]) + [2]) + [1]
#                        = [] + [3] + [2] + [1]
#                        = [3,2,1]

# 3b. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja iteracyjna.

def reverse_iter(list):
    start = []
    for i in list:
        start = [i] + start 
    return start
     
# 4a. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja rekurencyjna.

# 4b. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja iteracyjna.

 
# 5a. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja rekurencyjna.

# 5b. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja iteracyjna.

   
# 6a. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja rekurencyjna.

# 6b. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja iteracyjna.


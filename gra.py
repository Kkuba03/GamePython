from random import randint
#Celem gry jest odnalezienie klucza ukrytego na planszy 10x10 

count = 0                  #generowanie współrzędnych pozycji ukrytego klucza
while count <= 1:
    a = randint(1,10)
    b = randint(1,10)
    if (a == 1 and b == 1) or (a == 10 and b == 1) or (a == 1 and b == 10) or (a == 10 and b == 10):
        None
    else:
        count += 1
klucz = (a,b)

num = randint(1,4)     #losowanie narożnika
if num == 1:   
    start = (1,1)
elif num == 2:
    start = (10,10)
elif num == 3:
    start = (1,10)
else:
    start = (10,1)

print('Odnajdź ukryty na planszy klucz. Ruszaj sie używając W, A, S oraz D.')   #instrukcja dla gracza
count = 0
while start != klucz:                                                          
    odl = ((start[0] - klucz [0])**2 + (start[1] - klucz[1])**2)**(1/2)         #Odległość od klucza na początku gry
    print(f'Twoja pozycja: {start}')
    ruch = input("Wpisz litere: ")
    count += 1
    if ruch.lower() == 'w':                     
        if start[1]+1 <= 10:
            start = (start[0], start[1] + 1)
        else:
            print('Nie możesz pójść wyżej niż 10')
    
    elif ruch.lower() == 'a':
        if start[0]-1 >= 1:
            start = (start[0] - 1, start[1])
        else:
            print('Nie możesz pójść niżej niż 1')
    
    elif ruch.lower() == 's':
        if start[1]-1 >= 1:
            start = (start[0], start[1]-1)
        else:
            print('Nie możesz pójść niżej niż 1')
    
    elif ruch.lower() == 'd':
        if start[0]+1 <= 10:
            start = (start[0] + 1, start[1])
        else:
            print('Nie możesz pójść wyżej niż 10')
    odl2 = ((start[0] - klucz [0])**2 + (start[1] - klucz[1])**2)**(1/2)        #odległość od klucza po wykonanym ruchu
    if odl < odl2:
        print('Zimniej')                   
    elif odl2 < odl:
        print('Cieplej')
if start == klucz:
    print(f'Odnalazłeś klucz ukryty na pozycji {klucz} za {count} razem')
    





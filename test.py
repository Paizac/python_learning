import getpass
wyniki_gracz1 = 0
wyniki_gracz2 = 0
elementy = ['nozyczki' , 'papier', 'kamien']

while wyniki_gracz1 != 3 and wyniki_gracz2 != 3:
    
    poprawny_wybor = True
    while poprawny_wybor:
        wybor_gracz1 = getpass.getpass('Gracz1 podaj swoj wybor : ')
        if wybor_gracz1 in elementy:
            poprawny_wybor = False

    poprawny_wybor = True
    while poprawny_wybor:
        wybor_gracz2 = getpass.getpass('Gracz2 podaj swoj wybor : ')
        if wybor_gracz2 in elementy:
            poprawny_wybor = False


    if wybor_gracz1 == 'kamien' and wybor_gracz2 == 'nozyczki' or wybor_gracz1 == 'papier' and wybor_gracz2 == 'kamien' or wybor_gracz1 == 'nozyczki' and wybor_gracz2 == 'papier':
        print ('Wygral Gracz1')
        wyniki_gracz1 +=1
    elif wybor_gracz1 == wybor_gracz2:
        print('Remis')
    else :
        print ('Wygral Gracz2')
        wyniki_gracz2 +=1
if wyniki_gracz1 > wyniki_gracz2:
    print ('Prezydentem zostaje Gracz1')
else :
    print ('Prezydentem zostaje Gracz2')
    
from random import randrange
import random
import os

print('''


Répondre par oui / non sauf pour la longeur


''')

while True :

    length = 0
    loop = 0
    password = ''
    listall = []
    yes = 'autre'

    letterMajL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    numberL = ['0', '1','2', '3', '4', '5', '6', '7', '8', '9']


    caractereL = ['''!''', '''@''', '''#''', '''$''', '''%''', '''^''', '''&''', '''*''', '''(''', ''')''', '''_''', '''-''', '''+''', '''=''', '''{''', '''[''', '''}''', ''']''', '''|''', ''':''', ''';''', '''"''', '''<''', ''',''', '''>''', '''.''', '''?''', '''/''']


    letterL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
    
    letter = 'peut-être'
    letterMaj = 'peut-être'
    number = 'peut-être'
    caractere = 'peut-être'


    while yes != 'oui' :
        letter = input('''Voulez-vous des lettres minuscules ?
''')
        if letter == 'oui' or letter == 'non' : 
            yes = 'oui'

  
    if letter == 'oui' :
        listall = listall + letterL


    yes = 'peut-être'

    while yes != 'oui' :
        letterMaj = input('''Voulez-vous des lettres majuscules ?
''')
        if letterMaj == 'oui' or letterMaj == 'non' : 
            yes = 'oui'

    if letterMaj == 'oui' :
        listall = listall + letterMajL


    yes = 'peut-être'

    while yes != 'oui' :
        number = input('''Voulez-vous des chiffres ?
''')
        if number == 'oui' or number == 'non' : 
            yes = 'oui'

    if number == 'oui' :
        listall = listall + numberL


    yes = 'peut-être'

    while yes != 'oui' :
        caractere = input('''Voulez-vous des caractères spéciaux?
''')
        if caractere == 'oui' or caractere == 'non' : 
            yes = 'oui'

    if caractere == 'oui' :
        listall = listall + caractereL


    length = input('''Combien de caractère voulez-vous au total
''')

    lengthVerif = (length.isnumeric())

    if lengthVerif == True :

        while loop < int(length) :
            
            password = password + random.choice(listall)

            loop = loop + 1
        print('''
        
''')
        print(password)
        print('''
''')
        input('''C'est bon?''')
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''


Répondre par oui / non sauf pour la longeur


''')

    else :
        print("Tu n'as pas entré une longeur de mot de passe")
        print('''
''')

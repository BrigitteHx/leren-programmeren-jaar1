# M05.D01.O8 - Game over! - Retry

from funtionsforthegame2 import *

while game:
    antwoord1 = inleiding()
    if antwoord1 in yes:
        naam()
        chapter1()
        antwoord2 = ABCkeuze()
        if antwoord2 in a or antwoord2 in c:
            chapter1_option1()
            antwoord4 = ABCkeuze()
        elif antwoord2 in b:
            chapter1_option2()
            antwoord3 = YNkeuze()
            if antwoord3 in yes:
             chapter1_badending()
             game = False
            elif antwoord3 in no:
             chapter1_goodeding()
             game = False
        if antwoord4 in c: 
            chapter2_semigoodending()
            game = False
        elif antwoord4 in a or antwoord4 in b:
            chapter2_continue()
            antwoord5 = ABkeuze()
            if antwoord5 in a:
                chapter3_badending()
                game = False
            elif antwoord5 in b:
                chapter3_goodending()
                game is False
    if game == False:
        print("Wilt u nog een keer spelen? ")
        antwoord6 = YNkeuze()
        if antwoord6 in yes: 
            game = True
        else: 
            exit()

# M05.D01.O8 - Game over! - Retry?
from time import sleep

# functions: 
# INLEIDING 

def inleiding():
    inleiding_answer = input("Welcome to the Maze of Madness, are you ready to play? (y/n) ").lower()
    return inleiding_answer

def naam():
    naam_invoer = input("There's no turning back now but before you enter the maze, what is your name? ")
    return naam_invoer

def ABCkeuze():
    keuze = input("A, B of C? ").lower()
    return keuze

def ABkeuze():
    keuze = input("A of B? ").lower()
    return keuze

def YNkeuze():
    keuze = input("Yes or no? ").lower()
    return keuze

# CHAPTERS
def chapter1():
    print("""
    Alright then, you're standing in front of the maze and you can see the 3 ways right in front of you..
    
    A. What might be laying around that corner? I'm going right!
    B. I'd like to see more of the Maze, I'm going straight forward. 
    C. But what about left? What will I find there? I'm going to find that out. 
       """)

def chapter1_option1():
    print("""
    On the way you come across another intersection..
    
    
    A. You choose to ignore the other ways and follow the route, lets go!
    B. You're going left, what will that way bring you to?
    C. That one bush doesn't look so stable, you're not liking this maze very much and decide to climb over it.. 
    """)

def chapter1_option2():
    print("""
    So you've decided to keep going?
    Thats great, while you're walking forward you notice something in the distance.
    Coming closer you realise its an apple tree! 

    Those apples look really good, would you like to take a break and eat some? (y/n) 
    """)

def chapter1_badending():
     print("""
    Didnt I mention that you should ever trust a maze?! 
    The apples end up being poisened and you die. 
    
    Congratulations, you unlocked the BAD ending.
    
    Not that you should be proud of it.. Better luck next time!
    """)

def chapter1_goodeding():
    print(""" 
    Nice decision to see through that, those apples were poisened! ")
    You kept walking and walked straight into victory!")
    
    Good job, you found the exit and unlocked the GOOD ENDING!
    """)

def chapter2_semigoodending():
    print("""
    Oh no! You while you climbed over the bush you hurt yourself, a sprained ankle is never nice.
    At least you made it out of the maze quickly, congrats! You earned the *semi-good* ending.
    """)
    
def chapter2_continue():
    print("""You've been on your way a little while when you a bridge in the distance.
    You could also still follow the route.

    So, your options are: 
    
    A. Im up for a risk and I'm going for the bridge! 
    B. Im not so sure about that bridge and I'd rather follow the route. 
    """)

def chapter3_badending():
    print("""
    So you're a though one? Crossing a bridge in a maze, I havent seen a lot people do that before.
    Too bad for you, you shouldn't have done it either...
    
    CRACK!

    You fell through the bridge and earned the *bad ending*.
    """)

def chapter3_goodending():
    print("""
    Very, very wise descision to follow the route, that bridge wasnt stable at all.
    You kept going straight to the exit and found the exit!
    Congrats, you unlocked the *good ending*! Have a wonderful rest of your day.""")


# variabelen:
yes = ("yes", "y")
no = ("no", "n")
# a = "a"
# b = "b"
# c = "c"
# d = "d"
game = True


# code:

while game:
    antwoord1 = inleiding()
    if antwoord1 in yes:
        naam()
        chapter1()
        antwoord2 = ABCkeuze()
        if antwoord2 == "a" or antwoord2 == "c":
            chapter1_option1()
            antwoord4 = ABCkeuze()
        elif antwoord2 == "b":
            chapter1_option2()
            antwoord3 = YNkeuze()
            if antwoord3 == "y":
             chapter1_badending()
             game = False
            elif antwoord3 == "n":
             chapter1_goodeding()
             game = False
        if antwoord4 == "c": 
            chapter2_semigoodending()
            game = False
        elif antwoord4 == "a" or antwoord4 == "b":
            chapter2_continue()
            antwoord5 = ABkeuze()
            if antwoord5 == "a":
                chapter3_badending()
                game = False
            elif antwoord5 == "b":
                chapter3_goodending()
                game is False
    if game == False:
        print("Wilt u nog een keer spelen? ")
        antwoord6 = YNkeuze()
        if antwoord6 == "y": 
            game = True
        else: 
            exit()

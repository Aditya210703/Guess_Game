"""
Created on Sun Dec 25 22:25:35 2022

@author: Aditya verma
"""

# Intro func.


def intro():
    print("Welcome to the game\n")
    print("In this Game you have to guess a three numbers combination ranging between 0 to 9\n")
    print("some clues will be provided to you \n")
    print("The possible clues are: \n ○ Close: You've guessed a correct number but in the wrong position. \n ○ Match: You've guessed a correct number in the correct position. \n ○ Match1: You've guessed two correct numbers in the correct positions. \n ○ 👎: You haven't guess any of the numbers correctly.")
    print("\nSo let's Start The Game")


# checking wether right or wrong input


def chk(a, b, c):
    if (type(10) == type(a) and type(10) == type(b) and type(10) == type(c)):
        if ((a < 10 and a >= 0) and (b < 10 and b >= 0) and (c < 10 and c >= 0)):
            return True
        else:
            return False
    else:
        return False


# Func. to generate Random Integer


def ran():

   # generate random integer values
    import random
    # generate some integers
    l = []
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    l.extend([a, b, c])

    return l


# Functio to give clues


def clue(a, b, c, l):
    c_name = 'Close'
    m = 'Match'
    m_n = 'Match 1'
    n = 'Nope'
    b_name = 'cracked'
    i = 0
    if ((l[i] == a) & (l[i+1] == b) & (l[i+2] == c)):
        print("Boom!!! You Cracked It")
        return b_name
    elif ((l[i] == a) & (l[i+1] == b)):
        print(m_n)
        return m
    elif (((l[i+1] == b) & (l[i+2] == c))):
        print(m_n)
        return m
    elif ((l[i] == a) & (l[i+2] == c)):
        print(m_n)
        return m
    elif ((l[i] == a) | (l[i+1] == b) | (l[i+2] == c)):
        print(m)
        return m
    elif (l[i] == b or l[i] == c):
        print(c_name)
        return c_name
    elif (l[i+1] == a or l[i+1] == c):
        print(c_name)
        return c_name
    elif (l[i+2] == b or l[i+2] == a):
        print(c_name)
        return c_name
    else:
        print("👎")
        return n


# Main Function


l = ran()
intro()
f = ''
s = 'cracked'
while (f != s):
    print("\nWhat is Your Guess: ?")
    print("\nEnter three numbers")
    a, b, c = [int(i) for i in input().split()]
    t = chk(a, b, c)
    if (t == False):
        while (t != True):
            print("\nWrong Input. \n Enter three numbers")
            a, b, c = [int(i) for i in input().split()]
            t = chk(a, b, c)
    f = clue(a, b, c, l)
    print("Press 1 to know the answer or press 0.")
    j = int(input())
    if j == 1:
        print(l)
        f = 'cracked'

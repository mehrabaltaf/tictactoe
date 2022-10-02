import numpy as np
import random
T =np.array([["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]])
a= [1,2,3,4,5,6,7,8,9]
def sg(array):
    print(f" {array[0][0]} | {array[0][1]} | {array[0][2]} ")
    print(f"----------")
    print(f" {array[1][0]} | {array[1][1]} | {array[1][2]} ")
    print(f"----------")
    print(f" {array[2][0]} | {array[2][1]} | {array[2][2]} ")


def state():
    a = input("1=New game 2=Quit: ")
    if a == "1":
        s=input("1=Vs CPU 2=Multiplayer: ")
        if s=="1":
            game1()
        elif s=="2":
            game()
        else:
            print("Invalid input")
            state()

    elif a == "2":
        quit()
    else:
        print("Invalid input")
        state()


def draw(array):
    if array==[]:
        print("Draw")
        return True


def check(array,sym,opponent):
    if ((array[0][0]==array[1][0]==array[2][0]==sym) or (array[0][1]==array[1][1]==array[2][1]==sym) or (array[0][2]==array[1][2]==array[2][2]==sym) or (array[0][0]==array[0][1]==array[0][2]==sym) or (array[1][0]==array[1][1]==array[1][2]==sym) or (array[2][0]==array[2][1]==array[2][2]==sym) or (array[0][0]==array[1][1]==array[2][2]==sym) or (array[0][2]==array[1][1]==array[2][0]==sym)) and sym=="x" and opponent=="p1" :
        print("player 1 wins")
        return True

    if ((array[0][0]==array[1][0]==array[2][0]==sym) or (array[0][1]==array[1][1]==array[2][1]==sym) or (array[0][2]==array[1][2]==array[2][2]==sym) or (array[0][0]==array[0][1]==array[0][2]==sym) or (array[1][0]==array[1][1]==array[1][2]==sym) or (array[2][0]==array[2][1]==array[2][2]==sym) or (array[0][0]==array[1][1]==array[2][2]==sym) or (array[0][2]==array[1][1]==array[2][0]==sym)) and sym=="o" and opponent=="cpu":
        print("cpu wins")
        return True

    if ((array[0][0]==array[1][0]==array[2][0]==sym) or (array[0][1]==array[1][1]==array[2][1]==sym) or (array[0][2]==array[1][2]==array[2][2]==sym) or (array[0][0]==array[0][1]==array[0][2]==sym) or (array[1][0]==array[1][1]==array[1][2]==sym) or (array[2][0]==array[2][1]==array[2][2]==sym) or (array[0][0]==array[1][1]==array[2][2]==sym) or (array[0][2]==array[1][1]==array[2][0]==sym)) and sym=="o" and opponent=="p2":
        print("player2 wins")
        return True


def player(array,val,sym):
    array[array == val] = sym
    sg(array)

def player1retry(array,arr):
    print("Player 1>", end="")
    number = input("")
    if int(number) in arr:
        arr.remove(int(number))
        player(array, number, "x")
        if check(array, "x", "p1"):
            print()
            state()
        elif draw(arr):
            print()
            state()
    else:
        print("Invalid input")
        player1retry(array, arr)

def player2retry(array,arr):
    print("Player 2>", end="")
    number = input("")
    if int(number) in arr:
        arr.remove(int(number))
        player(array, number, "o")
        if check(array, "o", "p2"):
            print()
            state()
        elif draw(arr):
            print()
            state()
    else:
        print("Invalid input")
        player2retry(array, arr)


def cpu(array,arr):
    print("CPU> ")
    p = random.choice(arr)
    arr.remove(p)
    player(array, str(p), "o")
    if check(array, "o", "cpu"):
        print()
        state()
    elif draw(arr):
        print()
        state()


def game1():
    global T
    global a
    print("Start Game")
    sg(T)
    s = random.randint(0, 1)
    if s == 0:
        for i in range(1, 10):
            if i % 2 != 0:
                cpu(T,a)
            else:
                player1retry(T,a)

    elif s == 1:
        for i in range(1, 10):
            if i % 2 != 0:
                player1retry(T, a)
            else:
                cpu(T, a)


def game():
    global T
    global a
    print("Start Game")
    sg(T)
    for i in range(1,10):
        if i%2==0:
            player2retry(T,a)
        else:
            player1retry(T,a)


state()


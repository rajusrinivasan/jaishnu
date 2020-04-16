import random
import turtle

pen = turtle.Pen()
pen.color("brown")


def run_game():
    comp = random.randrange(1, 3)
    print("you are the player")
    print("1=rock")
    print("2=paper")
    print("3=scissor")
    player = int(input("1,2 or 3"))
    if comp == player:
        print("Draw !")
        draw()
    elif (comp + player) == 4:
        if comp < player:
            print("comp wins !")
            computer_wins()
        else:
            print("player wins !")
            player_wins()
    elif (comp + player) == 3:
        if comp < player:
            print("player wins !")
            player_wins()
        else:
            print("comp wins !")
            computer_wins()
    elif (comp + player) == 5:
        if comp < player:
            print("player wins!")
            player_wins()
        else:
            print("comp  wins!")
            computer_wins()

    print("the computer chose")
    print(comp)
    rps_game_board()
    print_game(comp, player)


def print_game(comp1, player1):
    if comp1 == 1:
        pen.up()
        pen.goto(150, 50)
        pen.down()
        rock()
    elif comp1 == 2:
        pen.up()
        pen.goto(150, 50)
        pen.down()
        paper()
    elif comp1 == 3:
        pen.up()
        pen.goto(150, 50)
        pen.down()
        scissor()
    if player1 == 1:
        pen.up()
        pen.goto(-150, 40)
        pen.down()
        rock()
    elif player1 == 2:
        pen.up()
        pen.goto(-150, 40)
        pen.down()
        paper()
    elif player1 == 3:
        pen.up()
        pen.goto(-150, 40)
        pen.down()
        scissor()


def draw():
    pen.up()
    pen.goto(0, -200)
    pen.down()
    pen.color('black')
    style = ('Courier', 30, 'italic')
    pen.write('draw', font=style, align='center')
    pen.hideturtle()


def computer_wins():
    pen.up()
    pen.goto(0, -200)
    pen.down()
    pen.color('black')
    style = ('Courier', 30, 'italic')
    pen.write('computer wins', font=style, align='center')
    pen.hideturtle()


def player_wins():
    pen.up()
    pen.goto(0, -200)
    pen.down()
    pen.color('black')
    style = ('Courier', 30, 'italic')
    pen.write('computer', font=style, align='center')
    pen.hideturtle()


def rps_game_board():
    pen.up()
    pen.goto(250, 200)
    pen.down()
    pen.color('black')
    style = ('Courier', 30, 'italic')
    pen.write('computer', font=style, align='center')
    pen.hideturtle()
    pen.up()
    pen.goto(-250, 200)
    pen.down()
    pen.color('black')
    style = ('Courier', 30, 'italic')
    pen.write('player', font=style, align='center')


def rock():
    for i in range(50):
        pen.color("brown")
        pen.width(5)
        pen.forward(100)
        pen.left(80)


pen.color("black")


def paper():
    for i in range(4):
        pen.color("green")
        pen.forward(200)
        pen.left(90)


def scissor():
    pen.speed(0)
    pen.color("black")
    pen.goto(-200, 50)
    pen.width(10)
    pen.circle(60)
    pen.up()
    pen.right(90)
    pen.forward(60)
    pen.down()
    pen.circle(60)
    pen.circle(60, 180)
    pen.right(50)
    pen.width(10)
    pen.forward(110)
    pen.left(120)
    pen.forward(135)
    pen.up()
    pen.left(180)
    pen.forward(135)
    pen.down()
    pen.left(60)
    pen.forward(150)
    pen.up()
    pen.left(180)
    pen.forward(150)
    pen.down()
    pen.left(110)
    pen.forward(150)
    pen.up()
    pen.goto(0, 0)
    pen.forward(60)
    pen.down()


run_game()

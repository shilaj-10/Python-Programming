import random

player1_total = 0
player2_total = 0

turn = 1

max_score = 20
''''
while player1_total<max_score and player2_total<max_score:
    choice = input("enter 'r' to roll or 'h' to hold")
    val = random.randint(1, 6)
    if choice=='r':
        player1_total=val+player1_total

    print(player1_total)
'''
while True:
    choice = input('[player {}] roll or hold[r/h]'.format(turn))
    value = random.randint(1, 6)
    if choice =='r':
        print ('player{} rolls{}'.format(turn,value))
        if value != 1:
            if turn==1:
                player1_total = value + player1_total
            else:
                player2_total = value + player2_total
        else:
            print ('player {} holds'.format(turn))
            if turn==1:
                player1_total=0
                turn = 2
            else:
                player2_total = 0
                turn = 1
    else:
        if turn == 1:
            turn = 2
        else:
            turn = 1
    # check if someone wins the game 
    if player1_total >= max_score or player2_total >= max_score:
        break 

if player1_total >= max_score:
    print ('player 1 wins!!!')
else:
    print('player 2 wins!!!')
#2 players =>
#dice roll
#player1_pos = 0
#snakes => 
#ladders

import random as rn

snakes = {54: 2, 99: 1, 78: 34, 46: 12, 82: 20, 30: 13}
ladders = {35: 45, 3: 19, 42: 52, 70: 83}

def update_position(current_pos):
    if current_pos in snakes:
        print(current_pos, "Daridram kottesidhi")
        return snakes[current_pos]
    
    if current_pos in ladders:
        print(current_pos, "Nakka thoka thokkav")
        return ladders[current_pos]
    
    return current_pos


player1_name = input("Enter player1 name")
player2_name = input("Enter player2 name")
player1_pos = 0
player2_pos = 0
turn = 1


while player1_pos < 100 and player2_pos < 100:
    dice_score = rn.randint(1, 6)
    if turn == 1:
        player1_pos += dice_score if dice_score + player1_pos <= 100 else 0
        #player_pos
        print(player1_name, 'at', dice_score, player1_pos)
        player1_pos = update_position(player1_pos)

        if dice_score != 6:
            turn = 2
    else:
        player2_pos += dice_score if dice_score + player2_pos <= 100 else 0
        print(player2_name, 'at', dice_score, player2_pos)
        player2_pos = update_position(player2_pos)

        if dice_score != 6:
            turn = 1


if player1_pos == 100:
    print(player1_name, "is the winner")
else:
    print(player2_name, "is the winner")
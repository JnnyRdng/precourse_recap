"""
simple game using conditionals in python
    pokemon battle!
"""

pikachu_health = 50
charmander_health = 50

inferno_pp = 1
flamethrower_pp = 1

# explain the game to the user
print ("Pikachu wants to battle!")
print("Fight!")

# Ask player for move to play
player_move = input("Which move do you wish to play?\nInferno ("+str(inferno_pp)+"PP):\nFlamethrower ("+str(flamethrower_pp)+"PP):\n")
# transform input to lowercase, input now case in-sensitive
player_move = player_move.lower()
if player_move == "inferno":
    # 'inferno' is a valid move, damage pikachu and remove 1 pp from that move
    print("Charmander used Inferno!")
    inferno_pp -= 1
    pikachu_health -= 25
elif player_move == "flamethrower":
    # 'flamethrower' is a valid move, damage pikachu and remove 1 pp from that move
    print("Charmander used Flamethrower!")
    flamethrower_pp -= 1
    pikachu_health -= 30
else:
    # not a valid move, turn over
    print("That's not a move!")

# computer has a turn, charmander gets damaged
print("Pikachu is up!")
print("Pikachu used Thunderbolt!")
charmander_health -= 35


# player has another turn, is asked again to select a move and input transformed to lowercase
print("Charmander is up!")
player_move = input("Which move do you wish to play?\nInferno ("+str(inferno_pp)+"PP):\nFlamethrower ("+str(flamethrower_pp)+"PP):\n")
player_move = player_move.lower()

# a valid move now requires enough PP left to use that move
if player_move == "inferno" and inferno_pp > 0:
    print("Charmander used Inferno!")
    pikachu_health -= 25
    if pikachu_health <= 0:
        # pikachu lost all his health!
        print("Pikachu fainted!")
        print("You win!")
    else:
        # pikachu still has some health and it's his turn!
        print("Pikachu used Shockwave!")
        charmander_health -= 20
        if charmander_health <= 0:
            print("Charmander fainted! You lose!")
elif player_move == "flamethrower" and flamethrower_pp > 0:
    print("Charmander used Flamethrower!")
    pikachu_health -= 30
    if pikachu_health <= 0:
        print("Pikachu fainted!")
        print("You win!")
    else:
        print("Pikachu used Shockwave!")
        charmander_health -= 20
        if charmander_health <= 0:
            print("Charmander fainted! You lose!")
else:
    # you didn't play a valid move, or that move didn't have any PP left
    if player_move == "inferno" or player_move == "flamethrower":
        # no pp left for that move
        print("That move is out of usable PP!")
    else:
        # not a valid move
        print("That's not a move!")
    # pikachu gets a turn and finishes you off
    print("Pikachu used Shockwave!")
    charmander_health -= 20
    if charmander_health <= 0:
        print("Charmander fainted! You lose!")





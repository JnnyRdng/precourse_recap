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

player_move = input("Which move do you wish to play?\nInferno ("+str(inferno_pp)+"PP):\nFlamethrower ("+str(flamethrower_pp)+"PP):\n")
# ask which move to play
   # damage pikachu based on move
   # move pp -= 1
if player_move == "inferno":
    print("Charmander used Inferno!")
    inferno_pp -= 1
    pikachu_health -= 25
elif player_move == "flamethrower":
    print("Charmander used Flamethrower!")
    flamethrower_pp -= 1
    pikachu_health -= 30
else:
    print("That's not a move!")

#computer has a turn
    # damage charmander based on move
    # move pp -= 1
print("Pikachu is up!")
print("Pikachu used Thunderbolt!")
charmander_health -= 35


# player has another turn
print("Charmander is up!")
player_move = input("Which move do you wish to play?\nInferno ("+str(inferno_pp)+"PP):\nFlamethrower ("+str(flamethrower_pp)+"PP):\n")
    # check pp
        # skip go if pp == 0
        # computer plays again
        # charmander fainted!
    # else play move
        # check if health is all gone
            # you won!
if player_move == "inferno" and inferno_pp > 0:
    print("Charmander used Inferno!")
    pikachu_health -= 25
    if pikachu_health <= 0:
        print("Pikachu fainted!")
        print("You win!")
    else:
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
    if player_move == "inferno" or player_move == "flamethrower":
        print("That move is out of usable PP!")
    else:
        print("That's not a move!")
    print("Pikachu used Shockwave!")
    charmander_health -= 20
    if charmander_health <= 0:
        print("Charmander fainted! You lose!")





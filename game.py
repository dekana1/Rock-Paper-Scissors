import random


score = 0

name = input("Enter your name:")
print("Hello,", name)

file = open("rating.txt", "r")
for line in file:
    info = line.split()
    if info[0] == name:
        score = int(info[1])

players_choices = input("specify choices").split(",")
default_choices = ["rock", "paper", "scissors"]
print("Okay, let's start")

if players_choices == [""]:
    possible_choice = default_choices
else:
    possible_choice = players_choices
computers_move = random.choice(possible_choice)

while True:
    player_move = input("Make a move")

    if player_move == "!exit":
        print("Bye!")
        break
    if player_move == "!rating":
        print("Your rating:", score)
        continue
    if player_move not in possible_choice:
        print("Invalid input")
        continue

    player_index = possible_choice.index(player_move)
    result_list = (possible_choice[player_index + 1:] + possible_choice[:player_index])

    if computers_move in result_list[len(result_list) // 2:]:
        print(f"Well done. Computer chose {computers_move} and failed")
        score += 100
    elif computers_move in result_list[:(len(result_list) // 2)]:
        print(f"Sorry, but computer chose {computers_move}")
    else:
        print(f"There is a draw ({computers_move})")
        score += 50

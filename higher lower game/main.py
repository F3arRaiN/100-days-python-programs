import html
from email import header

import art
import game_data
import random

# selects random item from the data list
def famous_selector():
    random_item = random.choice(game_data.data)
    return random_item
# aa

# returns the details of famous
def show_details(famous):
    data = ""
    for item in famous:
        if item == "follower_count":
            continue
        data += famous[item]
        data += ", "

    data = data[0:-2:1]
    data += "."
    return data

# checks the most famous amongst items
def most_famous(famous1, famous2):
    if famous1["follower_count"] > famous2["follower_count"]:
        return famous1
    else:
        return famous2

# compares if user is correct

# checks user selection
def usr_choice(famous1, famous2, usr_selection):
    choice = str(usr_selection)
    if choice == "a":
        choice = famous1
    else:
        choice = famous2

    return choice

famous1 = famous_selector()
score1 = 0
running = True
while running:
    # gives random data

    famous2 = famous_selector()

    #user score


    # print logo
    print(art.logo)

    # print first person
    print(f"Compare A: {show_details(famous1)}")

    # print vs
    print(art.vs)

    # print second person
    print(f"Against B: {show_details(famous2)}")

    # ask who has more followers
    usr_response = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*10)
    usr_selection = usr_choice(famous1, famous2, usr_response)


    if usr_selection == most_famous(famous1, famous2):

        score1 += 1
        print(f"You're Right! Current Score is: {score1}")
    else:
        print("Game over")
        break

    famous1 = famous2


import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TO DO-1: - Use a while loop to let the user guess again.
correct_letters = []
game_on = True
while game_on:
    guess = input("Guess a letter: ").lower()
    display = ""
    if "_" in display:
        game_on = False
    # TO DO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
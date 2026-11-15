import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

correct_letters = []
while lives > 0:
    guess = input("Guess a letter: ").lower()
    display = ""
    

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word and guess not in correct_letters:
        print(f"you have chosen {guess}, it is not in the word. You lose a life")
        lives -= 1
    elif "_" not in display:
        print("Congradulations you have won.")
        lives = 0
    else:
        print(f"You've already guessed {guess}")
        
    print(display)    
    print(stages[lives])        
    print(F"{lives}/6 lives left")
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
    


    
    if guess in correct_letters:
            print(f"You've already guessed {guess}")
            print(stages[lives])
            print(display)
    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        if guess in chosen_word:
            print(display)
            
        else:
            print(f"you have chosen {guess}, it is not in the word. You lose a life")
            lives -= 1
            
    print(stages[lives])        
    print(F"{lives}/6 lives left")
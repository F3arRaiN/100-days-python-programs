import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

response = int(input("Choose between 'rock', 'paper' and 'scissors'. Choose 0, 1 or 2 respectively: "))
options = [rock, paper, scissors]
computer_choice = random.choice(options)

if options[response] == computer_choice:
    print("Your choice:")
    print(options[response])
    print("Computer's choice:")
    print(computer_choice)
    print("It's a Draw")
elif options[response] == rock:
    if computer_choice == paper:
        print("Your choice:")
        print(options[response])
        print("Computer's choice:")
        print(computer_choice)
        print("You lose.")
    else:
        print("Your choice:")
        print(options[response])
        print("Computer's choice:")
        print(computer_choice)
        print("You win.")
elif options[response] == paper:
    if computer_choice == rock:
        print("Your choice:")
        print(options[response])
        print("Computer's choice:")
        print(computer_choice)
        print("You win.")
    else:
        print("Your choice:")
        print(options[response])
        print("Computer's choice:")
        print(computer_choice)
        print("You lose.")
elif options[response] == scissors:
    if computer_choice == paper:
        print("Your choice:")
        print(options[response])
        print("Computer's choice:")
        print(computer_choice)
        print("You win.")
    else:
        print("Your choice:")
        print(options[response])
        print("Computer's choice:")
        print(computer_choice)
        print("You lose.")
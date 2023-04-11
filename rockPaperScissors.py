#python rock paper scissors


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

#Write your code below this line 👇
import random

userChoice = int(input('what do you choose? 0 for rock, 1 for paper, 2 for scissors: '))


if userChoice == 0:
  print(f'player chooses ROCK {rock}')
  
elif userChoice == 1:
    print(f'player chooses PAPER {paper}')
  
elif userChoice == 2: 
  print(f'player chooses SCISSORS {scissors}')
else:
  print('please choose a valid entry')

computerChooses = random.randint(0, 2)

if computerChooses == 0:
  print(f'computer chooses ROCK {rock}')
  
elif computerChooses == 1:
    print(f'computer chooses PAPER {paper}')
  
else: 
  print(f'computer chooses SCISSORS {scissors}')


if userChoice == 0 and computerChooses == 2:
  print('Player beats computer')
elif userChoice == 2 and computerChooses == 1:
  print('Player beats computer')
elif userChoice == 1 and computerChooses == 0:
  print('Player beats computer')
elif userChoice == computerChooses:
  print('both players picked the same, no winner')
else: 
  print('Computer wins')

# again = input(int('play again?'))
# if again = 
name = input('What is your name?\n')
print('\n\nHi, %s.' % name + '\n\n' + 'this is a rock paper scissor game where a human player can compete against a computer. please follow instructions.\n')

# while human not chose 'no' as variable gameSwitch, keep on going
gameSwitch = ''
humanChoiceValidation = 1
humanPoints = 0
computerPoints = 0
while gameSwitch != 'no':
  
  # let human choose first 
  while humanChoiceValidation == 1:
    humanChoice = input('\ntype R for Rock, P for Papper, S for Scissors. press return\n')
    if humanChoice == 'R' or humanChoice == 'r': 
      print('\nhuman chose Rock')
      humanChoice = 1
      humanChoiceValidation = 0
    elif humanChoice == 'P' or humanChoice == 'p': 
      print('\nhuman chose Papper')
      humanChoice = 2
      humanChoiceValidation = 0
    elif humanChoice == 'S' or humanChoice == 's':
      print('\nhuman chose Scissors')
      humanChoice = 3
      humanChoiceValidation = 0
    else: 
      humanChoiceValidation = 1
    #print("\npress R for Rock, P for Papper, S for Scissors\n")

  # let computer choose now
  from random import randrange
  computerChoice = randrange(3) + 1
  if computerChoice == 1:
    print('computer chose Rock\n')
  elif computerChoice == 2:
    print('computer chose Paper\n')
  elif computerChoice == 3:
    print('computer chose Scissors\n')
  else:
    print('error\n')

  #print(type(humanChoice))
  #print(type(computerChoice))
  #print(humanChoice, ' ', computerChoice)

  # calculate winner, announce winner, increment points
  if humanChoice - computerChoice == 1 or humanChoice - computerChoice == -2:
    print('human wins this round\n')
    humanPoints += 1
  elif humanChoice - computerChoice == -1 or humanChoice - computerChoice == 2:
    print('computer wins this round\n')
    computerPoints += 1
  elif humanChoice - computerChoice == 0:
    print('draw\n')
  else:
    print('error\n')
    
  # ask if human want's to play more
  gameSwitch = input('does human want\'s to play more?\nyes/no\n')
  humanChoiceValidation = 1

print ('\nhuman : computer\n', humanPoints, ' : ', computerPoints)
if humanPoints > computerPoints:
  print('human win this game')
else:
  print('computer win this game')
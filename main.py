name = input('What is your name?\n')
print('\n\nHi, %s.' % name + '\n\n' + 'this is a rock paper scissor game where a human player can compete against a computer. please follow instructions.\n')

gameSwitch = '' # at the end of each round human makes a decision if want's to play more or not
humanChoiceValidation = False # is human's choice valid?
humanPoints = 0
computerPoints = 0
godmode = False # does human want's to cheat?

while gameSwitch != 'no':
  
  # let human choose first 
  while humanChoiceValidation == False:
    humanChoice = input('\ntype R for Rock, P for Papper, S for Scissors. press return\n')
    # convert human's choice to integer, validate choice, write choice on screen
    if humanChoice == 'R' or humanChoice == 'r': 
      print('\nhuman chose Rock')
      humanChoice = 1
      humanChoiceValidation = True
    elif humanChoice == 'P' or humanChoice == 'p': 
      print('\nhuman chose Papper')
      humanChoice = 2
      humanChoiceValidation = True
    elif humanChoice == 'S' or humanChoice == 's':
      print('\nhuman chose Scissors')
      humanChoice = 3
      humanChoiceValidation = True
    elif humanChoice == 'iddqd':
      godmode = 1
      humanChoiceValidation = False
    else: 
      humanChoiceValidation = False

  # let computer choose now
  from random import randrange # load random module
  computerChoice = randrange(3) + 1 # generate computer's choice
  # write computer's choice on screen in human readable form
  if computerChoice == 1:
    print('computer chose Rock\n')
  elif computerChoice == 2:
    print('computer chose Paper\n')
  elif computerChoice == 3:
    print('computer chose Scissors\n')
  else:
    print('error\n')

  #print(type(humanChoice)) # debug
  #print(type(computerChoice)) # debug
  #print(humanChoice, ' ', computerChoice) # debug

  # calculate winner, announce winner, increment points
  if godmode == True:
    print('human wins this round\n')
    humanPoints += 1
  elif humanChoice - computerChoice == 1 or humanChoice - computerChoice == -2:
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
  
  humanChoiceValidation = False

print ('\nhuman : computer\n', humanPoints, ' : ', computerPoints)
if humanPoints > computerPoints:
  print('human win this game')
else:
  print('computer win this game')
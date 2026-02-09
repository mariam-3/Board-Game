import random

game_running = True

# this is a list of random messages that could be displayed to the player
random_messages = [
    'Move back 3 squares.',
    'Move forward 4 squares.',
    'restart the game from round 1!',
    'Automatically finish your current round.',
    'All players move back 2 squares.',
    'All players restart the game.',
] 

# a function to create a unique random integer
def random_number(start, stop, not_equal=[]): 
  number = random.randint(start, stop)
  if number in not_equal:
    return random_number(start, stop, not_equal)
  else:
    return number

# The first square on which a random message will be displayed
random_square_1 = random_number(1, 21)

# The second square on which a random message will be displayed
random_square_2 = random_number(1, 21, [random_square_1])

# The third square on which a random message will be displayed
random_square_3 = random_number(1, 21, [random_square_1, random_square_2]) 

# a class to make it possible to have more than one player
class Player:
  def __init__(self, player_name, player_number):
    self.name = player_name
    self.number = player_number
    self.position = 0
    self.round = 1

# now, the number that will be generated will be in a range between the number the player provided and 1
dice = input('How many sides would you like your dice to have? ')

# Test if the input is a valid integer or not
while not isinstance(dice, int):
  try:
    # Try to convert the string to an integer
    dice = int(dice)
  except:
    # if the conversion is unsuccessful, ask the user to try again
    print('Invalid input. Try again.')
    dice = input('How many sides would you like your dice to have? ')

# so that we can call the right number of objects. 
player_count = input('How many players are participating today? ') 

# making that number an integar so that we can do math with it. 
player_count = int(player_count)

# creating a list... this will be empty for now
players = [] 

# a loop for the number of players
for i in range(player_count): 
  # the player number goes up each time
  player_number = i + 1
  # ask for the players' names
  player_name = input(f'What is the name of player {player_number}? ')
  # adds the information gathered above to a new object
  player = Player(player_name, player_number) 
  # adds the new player to the list created above
  players.append(player)

# start the game loop
while game_running:

  # a loop to give every player a turn
  for player in players:
    
    # ask the current player to choose to roll a number or quit
    print('------------------------------------')
    print(f"Player {player.name}'s turn. Enter r or q:")
    print('r : Roll a number.')
    print('q : Quit the game.')
    turn = input('>> ')

    # if the player doesn't enter a valid answer...
    while turn != 'r' and turn != 'q': 
      print('Sorry. That is an invalid answer. Please try again. ')
      # make them enter a valid one
      turn = input('>> ') 

    # if they want to quit...
    if turn == 'q': 
      # remove them from the list...
      players.remove(player) 
      # and let everyone else know
      print(f'Player {player.name} quit the game!') 

    # if they want to roll the die...
    elif turn == 'r': 
      # pick a random number between 1 and the number of faces on the die. 
      roll = random.randint(1, dice)
      # tells the player what they rolled
      print (f'you rolled a(n) {roll}') 
      # adds the new number to their total
      player.position += roll
      # tells them their new score
      print(f'You are now on round {player.round}, square {player.position}') 

      # if a player goes to position 16, we have a winner
      if player.position == 16:
        winner = player
        game_running = False
        break

      # if the player passed round 2 and doesn't reach position 16, they are out
      elif player.round >= 3:
          print('''Unfortunately, you haven't reached the 'win' square. 
          Good luck next time!''') 
          # removes the player from the list
          players.remove(player)
          print(player, "has been eliminated")

      # if the player's position is equal to any of the random numbers generated above...
      elif (player.position == random_square_1 or 
          player.position == random_square_2 or 
          player.position == random_square_3):
      
        # asks the player if they want to read the secret message
        read_message = input('''The square you have landed on has a hidden message. 
        Would you like to read it (y/n)?''')
      
        # if the answer is invalid
        while read_message != 'y' and read_message != 'n':
          # ask the player ot input a valid one
          print('Sorry. That is an invalid answer. Please try again. ') 
          turn = input('>> ')

        # if they said "yes"...
        if read_message == 'y':
          # a random one of the messages in the random_messages list above will be displayed
          random_message = random.choice(random_messages)
          print(random_message)
          
          # if the message is  'Move back 3 squares'...
          if random_message == random_messages[0]: 
            # they will move 3 steps backward 
            player.position -= 3
            # informs the player of their new position
            print('You are now on round ' + str(player.round) + ', square ' +str(player.position)) 

          # if the message is 'Move forward 4 squares'...
          elif random_message == random_messages[1]:
            player.position += 4
            print(f'You are now on round {player.round}, square {player.position}')

          # if the message is 'restart the game from round 1!'...
          elif random_message == random_messages[2]:
            player.round = 1
            player.position = 0
            print(f'You are now on round {player.round}, square {player.position}')
            print('You are now back on square 0')

          # if the message is 'Automatically finish your current round'...
          elif random_message == random_messages[3]:
            player.round += 1
            if player.round == 3:
              print('Sorry, you have lost the game!')
              print(f'You are now on round {player.round}, square {player.position}')

          # if the message is 'All players move back 2 squares.'...
          elif random_message == random_messages[4]:
            player.position -= 2
            print(f'You are now on round {player.round}, square {player.position}')
            for player in players:
              player.position -= 2

          # if the message is 'All players restart the game.'...
          elif random_message == random_messages[5]:
            for player in players:
              player.position = 0
              player.round = 1
              print(f'Player {player.name} is now on round {player.round}, square {player.position}.')
      
      # if have passed square 16...
      elif player.position > 16: 
        # tell them that they finished their round
        print('You have reached the end of the round') 
        player.round = int(player.round) 
        # adds 1 to their round number
        player.round += 1 
        # takes 16 away from their position (new position in the new round)
        player.position -= 16 
        # tells them their position
        print(f'your new position is round {player.round}, square {player.position}')

# when the game is over, the winner is announced.
print('-------------------------------------------')
print(winner.name, 'has won the game!')

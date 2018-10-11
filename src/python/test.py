#Import packages
import random
import sys

#Starting variables
starting_amount = 100
yes_no = ['yes', 'no']
bet_ = 0

#Starting message
while True: 
    play_game = input('Would you like to play a game?(yes or no): ')
    #Check for a valid response
    if play_game.lower() not in yes_no:
        print('Please input yes or no only')
    #If no, then break
    elif play_game.lower() == 'no':
        sys.exit(1)  
    #Otherwise start the game
    elif play_game.lower() == 'yes': 
        print("""Great! Welcome to the game 7 and 12. The rules are simple... You start with $100. 
              Each round you may bet up to the amount that you currently have. You will then roll 2 six-sided dice
              and add up their total. If you roll a 7 or a 12 you win and you double up. If you do not roll a 
              7 or a 12, you may choose to double your bet and roll a third die. If the sum of all three dice is 7 or 12
              you win. Other than that, you will lose the amount bet.""")
        break

bet(starting_amount)
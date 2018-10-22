#Kyle Chinn 10/10/2018 I have not given or received any unauthorized assistance on this assignment.  

#Import modules 
import random
import sys

#Starting variables
starting_amount = 100
yes_no = ['yes', 'no']

#Function for getting player bet
def bet(amount):
    current_amount = amount
    #Set allowable range for player bet amount
    bet_range = list(range(1, amount + 1))
    while amount > 1:
        #If player has < 1 exit program
        if amount < 1:
            print("Sorry you don't have anything left to bet...")
            print('')
            sys.exit(1)
        try:
            #Ask player for bet amount
            bet_ = input('You currently have' + ' ' + '$' + str(amount) + '. ' + 'How much would you like to bet? Please only use integers: ')
            if int(bet_) not in bet_range: 
                print('That is not an acceptable betting amount. How much would you like to bet?')
            #If bet is acceptable, pass it to bet_check()
            if int(bet_) in bet_range:
                bet_check(int(bet_), current_amount)
        except ValueError:
            print('Please use integers only...')
            continue
    return bet_

#Function for checking if bet is correct
def bet_check(current_bet, current_amount):
    while True:
        bet_check = input('You bet' + ' ' + '$' + str(current_bet) + ' ' + 'is that correct?(yes or no)')
        if bet_check.lower() not in yes_no:
            print('Please input yes or no only. You bet' + ' ' + '$' + str(current_bet) + ' ' + 'is that correct?(yes or no)')
        #If no send player back to bet()
        elif bet_check.lower() == 'no':
            bet(current_amount)
        #If yes call dice_roll() for the set bet amount
        elif bet_check.lower() == 'yes':
            dice_roll(current_bet, current_amount)

#Function for checking if player would like to continue
def keep_playing(amount):
    amount = amount
    while True:
        keep_playing = input('Would you like to keep playing?(yes or no)')
        if keep_playing.lower() not in yes_no:
            print('Please input yes or no only...')
        #if no then print final amount and exit program
        elif keep_playing.lower() == 'no':
            print('')
            print('You ended with' + ' ' + + '$' + str(amount) + '. Thanks for playing!')
            sys.exit()
        #if yes, call bet() with new amount
        elif keep_playing.lower() == 'yes':
            print('')
            bet(amount)
            return amount
        
#Dice roll function
def dice_roll(current_bet, amount):
    current_amount = amount
    #Random dice roll
    dice_1 = random.randrange(1,7)
    dice_2 = random.randrange(1,7)
    dice_3 = random.randrange(1,7)
    #Total roll
    tot_roll = dice_1 + dice_2
    print('')
    print('You rolled a' + ' ' + str(dice_1) + ' ' + 'and' + ' ' + 'a' + ' ' + str(dice_2) + ' ' + 'for a total of' + ' ' + str(tot_roll))
    #Check if total roll is either 7 or 12
    if int(tot_roll) == 7 or int(tot_roll) == 12:
        current_amount += current_bet
        print('Congratulations, you won! Your total amount is now' + ' ' + '$' + str(current_amount))
        print('')
        keep_playing(current_amount)
    #Check if player has any money left. If not, end the game
    if (current_amount - current_bet) < 1:
        print("Sorry you don't have anything left to bet...")
        print('')
        sys.exit(1)
    #Double up with third roll
    while True:
        third_roll = input("Sorry, you didn't win, would you like to double your bet and roll a third die?(yes or no)")
        #Check if doubling up would make player go under
        if (current_bet * 2) > current_amount and third_roll.lower() == 'yes':
            print('')
            print("Sorry you don't have enough money to bet that, you lost" + ' ' + '$' + str(current_bet) + '.')
            current_amount -= current_bet
            bet(current_amount)
            return current_amount
        #Only allow yes and no
        if third_roll.lower() not in yes_no: 
            print('Please input yes or no only...')
        #If no third roll, display current amount and prompt keep_playing()
        elif third_roll.lower() == 'no':
            current_amount -= current_bet
            print('')
            print('You have' + ' ' + '$' + str(current_amount) + ' ' + 'left.')
            keep_playing(current_amount)
            return current_amount
        #If yes, add third dice roll to tot_roll
        elif third_roll.lower() == 'yes':
            tot_roll += dice_3
            print('')
            print('Your third dice roll is a' + ' ' + str(dice_3) + ' ' + 'for a total of' + ' ' + str(tot_roll))
        #Check if total roll is either 7 or 12    
        if tot_roll == 7 or tot_roll == 12: 
            current_amount += current_bet * 2
            print('Congratulations, you won! Your total amount is now' + ' ' + '$' + str(current_amount))
            print('')
            keep_playing(current_amount)
            return current_amount
        #If not 7 or 12, subtract bet * 2 from current amount and prompt keep_playing()
        else:
            current_amount -= current_bet * 2
            print("Sorry you didn't win this time, you lost" + ' ' + '$' + str(current_bet * 2) + ' ' + 'leaving you with' + ' ' + '$' + str(current_amount) + '.')
            print('')
            keep_playing(current_amount)
            return current_amount

#Function for starting the game
def game():
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
            print("""
            
Great! Welcome to the game 7 and 12. The rules are simple... You start with $100. Each round you may bet up to the amount that you currently have. You will then roll 2 six-sided dice
and add up their total. If you roll a 7 or a 12 you win and you double up. If you do not roll a 
7 or a 12, you may choose to double your bet and roll a third die. If the sum of all three dice is 7 or 12
you win. Other than that, you will lose the amount bet.

""")
            break

    bet(starting_amount)
    
game()
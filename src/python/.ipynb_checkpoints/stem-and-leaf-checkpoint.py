#Kyle Chinn 10/10/2018 I have not given or received any unauthorized assistance on this assignment.

#NOTE: The professor gave me an extension on this homework since I was at a funeral for 5 days over the due date.

import pandas as pd
import subprocess
import sys

#The lxml package is needed for pandas to read the files from github
print('Checking dependecies...')
print('')
subprocess.call([sys.executable, '-m', 'pip', 'install', 'lxml'])
print('')

#Selection function
def selection():
    #Acceptable input list
    input_list = [1, 2, 3]
    while True:
        try:
            #Greet user and ask for selection
            user_num = input('Hello! I print out stem and leaf plots... Please select 1, 2, 3: ')
            #If input is not accetable, reissue prompt
            if int(user_num) not in input_list:
                print('Please input 1, 2, or 3 only')
            #If input is accetable, call stem() 
            elif int(user_num) in input_list:
                stem(user_num)
        #Catch ValueErrors
        except ValueError:
            print('Please input 1, 2, or 3 only')
            
#Function for printing stem and leaf plot
def stem(num):
    #Create empty dictionary
    dict = {}
    #Import file from github given user input
    file = pd.read_html('https://github.com/PixarJunkie/dsc-430-python-programming/blob/master/data/StemAndLeaf%d.txt' % (int(num)))
    #Get file into usable list format
    list_ = list(file[0][1])
    list_ = [list(str(item)) for item in list_]

    #Fill the dictionary
    for line in list_:
        #Set key, value from list_
        key = line[0]
        value = line[1]
        #If key doesn't exist yet, create it, and assign empty list for it's values
        if key not in dict:
            dict[key] = []
        #Add values to lists for each key
        dict[key].append(value)
    #Title
    print("""   Stem and Leaf Plot""")
    #Print stem and leaf plot
    for k, v in dict.items():
        #Print key: value while joining values and removing ','
        print('{}: {}'.format(k, ''.join(v)))
    #Prompt user for another selection or to quit
    another_selection()
    return None

#Function for checking if player would like to continue
def another_selection():
    #Acceptable input list
    yes_no = ['yes', 'no']
    while True:
        #Prompt user for selection
        new_selection = input('Would you like make another selection?(yes or no)')
        if new_selection.lower() not in yes_no:
            print('Please input yes or no only...')
        #If no, thank user and exit program
        elif new_selection.lower() == 'no':
            print('')
            print('Thanks for checking out the program, bye!')
            print('')
            sys.exit(1)
        #If yes, call selection()
        elif new_selection.lower() == 'yes':
            print('')
            selection()
            return None
        
selection()
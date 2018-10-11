#Kyle Chinn 10/10/2018 I have not given or received any unauthorized assistance on this assignment.  

#Import packages
import pandas as pd  
import string

#Alphabet
alphabet = list(string.ascii_lowercase)

#Last letter count function
def last_letter_count():
    #Create empty dictionaries 
    boy_dict = {}
    girl_dict = {}
    
    #Create name lists from github
    boys_git = pd.read_html('https://github.com/PixarJunkie/dsc-430-python-programming/blob/master/data/namesBoys.txt')
    boys_list = list(boys_git[0][1])
    girls_git = pd.read_html('https://github.com/PixarJunkie/dsc-430-python-programming/blob/master/data/namesGirls.txt') 
    girls_list = list(girls_git[0][1])
    
    #Get last letter of boy names
    for boy in boys_list:
        last_letter_boy = list(boy)[-1]
        #If last letter is already in boy_dict, increase current value by 1
        if last_letter_boy in boy_dict:
            boy_dict[last_letter_boy] += 1
        #If last letter is not in boy_dict, create key and set value = 1
        else: 
            boy_dict[last_letter_boy] = 1
    #Get last letter of girl names
    for girl in girls_list:
        last_letter_girl = list(girl)[-1]
        #If last letter is already in girl_dict, increase current value by 1
        if last_letter_girl in girl_dict: 
            girl_dict[last_letter_girl] += 1
        #If last letter is not in girl_dict, create key and set value = 1
        else:
            girl_dict[last_letter_girl] = 1
    
    #Create dataframe for output
    final_df = pd.DataFrame(columns = ['Ending', 'Boys', 'Girls'])
    final_df.Ending = alphabet
    #Map dicts to columns
    final_df.Boys = final_df.Ending.map(boy_dict)
    final_df.Girls = final_df.Ending.map(girl_dict)
    #Replace NaN with 0
    final_df.fillna(0, inplace = True)
    
    print(final_df)
    return final_df

    
last_letter_count()

#Observations: Out of the 2 thousand names looked at; last letters of girl names appear to use less of the alphabet than boys since there were a lot more 0 counts among girl names than boys. Both boys and girls had more frequent uses of the letters e and n than any of the other letters in the alphabet.The least commonly used letters among both boys and girls were f, j, u, and q (all were either 1 or 0)

#Kyle Chinn 10/13/2018 I have not given or received any unauthorized assistance on this assignment.

#NOTE: The professor gave me an extension on this homework since I was at a funeral for 5 days over the due date.

#Import packages
import pandas as pd
import statistics as stats
import csv
import sys
from math import sqrt

print('This program requires that "avocado.csv" exists in the directory which you are running "avocado.py" from')

#Set "gloabal" variables
yes_no = ['yes', 'no']
stat_list = ['mean', 'median', 'sd', 'hmean', 'hmedian', 'hsd']
#file_path = r'/Users/Luxo_Jr/Desktop/School/Fall 2018/dsc-430-python-programming/data/avocado.csv'
file_path = r'avocado.csv'
special_columns = ['date', 'year', 'type', 'region']

#Function for continuing 
def keep_going():
    while True:
        #Check if user wants to keep going
        cont_ = input('Would you like to start over?(yes or no): ')
        if cont_.lower() not in yes_no:
            print('Please input yes or no only')
        #Exit if user inputs no
        elif cont_.lower() == 'no':
            print('')
            print('Thanks, have a nice day!')
            sys.exit(1)
        #Run column_select if user inputs yes
        elif cont_.lower() == 'yes':
            column_select()
        return None

#Function for printing statistics
def stat(stat_selection, data, column_title):
    
    #If passed mean, check columns and print appropriate version
    if stat_selection == 'mean':
        #If it is a date or categorical column, print the mean of the count of each category or date
        if column_title in special_columns:
            #Create dataframe from data list and column_title
            df = pd.DataFrame(data, columns = ['%s' %(column_title)])
            #groupby each date or category and take the mean of the counts
            mean_ = df.groupby(['%s' % column_title])['%s' % column_title].count().mean()
            print('That is a date or categorical column so a mean is not available, but the mean value count of' + ' ' + column_title + ' ' + 'is' + ' ' + str(mean_))
        #If column_title is apprpriate, print normal mean
        elif column_title not in special_columns:
            #Convert list values to float
            data = [float(x) for x in data]
            print('The mean of' + ' ' + column_title + ' ' + 'is' + ' ' + str(stats.mean(data)))
        #Check if user wants to continue
        keep_going()
    #If pass hmean, check columns and print apprpriate version
    elif stat_selection == 'hmean':
        #With hmean, there is no use of pandas dataframes, so simply return no mean for date or categorical
        if column_title in special_columns:
            print('Sorry there is no homegrown mean for date or categorical columns.')
        #If column is apprpriate, sum the float values in data and divide by the length of data
        elif column_title not in special_columns:
            sum_ = sum([float(x) for x in data])
            hmean_ = sum_ / len(data)
            print('The mean of' + ' ' + column_title + ' ' + 'is' + ' ' + str(hmean_))
        #Check if user wants to continue
        keep_going()
        
    #If passed median, check columns and print appropriate version (same logic as mean so no additional comments)
    if stat_selection == 'median':
        df = pd.DataFrame(data, columns = ['%s' %(column_title)])
        median_ = stats.median(df['%s' %(column_title)])
        if column_title in special_columns:
            print('The median value of' + ' ' + column_title + ' ' + 'is' + ' ' + str(median_))
        elif column_title not in special_columns:
            print('The median of' + ' ' + column_title + ' ' + 'is' + ' ' +  str(median_))
        keep_going()
    #If passed hmedian
    elif stat_selection == 'hmedian':
        #Sort data and get index for middle value
        sorted_ = sorted(data)
        index_ = int((len(data) - 1) / 2)
        #If odd number of values in data, print the value at index_
        if len(data) % 2 == 1:
            hmedian_ = sorted_[index_]
            print('The median value of' + ' ' + column_title + ' ' + 'is' + ' ' + str(hmedian_))
        #If even number of values in data, get the sum of the 2 middle values and return the mean. If they're the same value, simply print the value of index_
        else:
            hmedian_1 = sorted_[index_] 
            hmedian_2 = sorted_[index_ + 1]
            if hmedian_1 == hmedian_2:
                print('The median value of' + ' ' + column_title + ' ' + 'is' + ' ' + str(hmedian_1))
            else:
                print('The median values of' + ' ' + column_title + ' ' + 'are' + ' ' + str(hmedian_1) + ' ' + 'and' + ' ' + str(hmedian_2))
        keep_going()
        
    #If passed sd, check columns and print appropriate version
    if stat_selection == 'sd':
        #If date or categorical, tell user it is not possible
        if column_title in special_columns:
            print('Sorry, that is a date or categorical column so the standard deviation is not computable...')
            keep_going()
        #Float values in data and print the standard deviation
        elif column_title not in special_columns:
            data = [float(x) for x in data]
            print('The stadard deviation of' + ' ' + column_title + ' ' + 'is' + ' ' + str(stats.stdev(data)))
        #Check if user wants to keep going
        keep_going()
    #If passed hsd, check columns and print appropriate version (same as above)
    elif stat_selection == 'hsd':
        if column_title in special_columns:
            print('Sorry, that is a date or categorical column so the standard deviation is not computable...')
            print('')
            keep_going()
        else:
            #Float values in data
            data = [float(x) for x in data]
            #Compute the mean for future calcs
            x_bar = sum([float(x) for x in data]) / len(data)
            #Compute the variance for future calcs
            var_x = sum([(float(x) - x_bar) ** 2 for x in data]) / (len(data) - 1)
            #Print standard deviation
            x_sd = sqrt(var_x)
            print('The stadard deviation of' + ' ' + column_title + ' ' + 'is' + ' ' + str(x_sd))
            print('')
            keep_going()
        return None

#Main function
def column_select():
     
    #Get column titles
    with open (file_path) as file:
        reader = csv.reader(file)
        #Fetch the first row
        column_labels = next(reader)
        #Lowercase all strings 
        column_labels = [x.lower() for x in column_labels]
        #Print available columns for user selection
        print("""Columns""")
        #Print without ',' or list brackets
        print('\n'.join(column_labels))
    while True:
        #Ask user to input column name
        column_name = input('Please input a column name from the list above: ')
        column_name = column_name.lower()
        #Check if user input is in column_labels
        if column_name not in column_labels:
            print('That column does not exist..')
        else:
            while True:
                #Check if user would like to rechoose column
                correct_column = input('You have selected' + ' ' + column_name + ' ' + 'is that correct?(yes or no): ')
                if correct_column.lower() not in yes_no:
                            print('Please input yes or no only...')
                elif correct_column.lower() == 'no':
                    column_select()
                #If user wants to continue, read data from the file where the index = column name
                elif correct_column.lower() == 'yes':
                    with open(file_path) as file_:
                        file_.readline()
                        data = []
                        for row in file_: 
                            data.append(row.split(',')[column_labels.index('%s' % (column_name))])
                    print('')
                    while True:
                        #Check which statistic the user wants to see
                        stat_select = input("""Which stat would you like to compute?:                            
1. mean
2. median
3. standard deviation (sd)
4. homegrown mean (hmean)
5. homegrown median (hmedian)
6. homegrown standard deviation (hsd)

Please only input mean, median, sd, hmean, hmedian, or hsd only: """)
                        #Check for appropriate input
                        if stat_select not in stat_list:
                            print('')
                            print('Please input mean, median, sd, hmean, hmedian, or hsd only: ')
                        #If input is correct, pass stat_select, data, and column_name to the stat function
                        elif stat_select in stat_list:
                            stat(stat_select, data, column_name)
                            
column_select()
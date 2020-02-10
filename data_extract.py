from datetime import datetime
import csv

def display_data(csv_file, n=0):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        csv_file: name of the city file we want to display
        n: number of time this function was already called before to display data
    Returns:
        (-)
    '''
    #we create a loop where function calls itself constantly and outprints 5 lines of data for a user, if asked so
    if n>0:
        k = 0
        with open(csv_file, 'r') as f_in:
            data_reader = csv.DictReader(f_in, delimiter = ',')
            for line in data_reader:
                if 5*(n-1) < k <= 5*n:
                    print(line)
                k += 1

    display = input('\nWould you like to view 5 more individual trip datas? Type \'yes\' or \'no\'.\n')
    if display == 'yes':
        print('fuction correctly enters this statement')
        display_data(csv_file, n+1)

display_data('washington.csv')

from datetime import datetime
import csv


def month_into_int(month_of_interest):
    if month_of_interest == 'January':
        return(1)
    elif month_of_interest == 'February':
        return(2)
    elif month_of_interest == 'March':
        return(3)
    elif month_of_interest == 'April':
        return(4)
    elif month_of_interest == 'May':
        return(5)
    elif month_of_interest == 'June':
        return(6)

def birth_years(city_file, time_period, month_of_interest = None, day_of_interest = None):
    birthdays = {}
    # open the file of interest and start reading it
    with open(city_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter = ',')
        for line in data_reader:
            # for each 3 types of sorting data
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:
                    # we extract the types of users that we have
                    current_birthday = line['Birth Year']
                        #here we check if this particular type of user is already in the dictionary
                    x = birthdays.get(current_birthday)
                    is_null = x is None
                        # if it is not in the dict, we add a Birth Year to dict and start a counter
                    if is_null:
                        birthdays[current_birthday] = 1
                    # if it already exist, we increment the value
                    else:
                        birthdays[current_birthday] += 1
                #similar procedure is performed for the daily sorting
            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:                    # we extract the types of users that we have
                    current_birthday = line['Birth Year']
                    x = birthdays.get(current_birthday)
                    is_null = x is None
                    if is_null:
                        birthdays[current_birthday] = 1
                    else:
                        birthdays[current_birthday] += 1
            # similar process if performed for none
            elif time_period == 'none':
                current_birthday = line['Birth Year']
                x = birthdays.get(current_birthday)
                is_null = x is None
                if is_null:
                    birthdays[current_birthday] = 1
                else:
                    birthdays[current_birthday] += 1
    return birthdays

the_users = birth_years('new_york_city.csv', 'month', 'January')
print(the_users)

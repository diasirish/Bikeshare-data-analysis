#import all necessary packages and functions
import csv, time
from datetime import date, datetime


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the string of the name of the city

    Args:
        none.
    Returns:
        (str) name of the city of interst.
    '''

    while True:         #Creating a loop to keep on asking a user for a correct input (in case, it is entered incorrectly)
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

        try:        #Try to avoid errors that may arise from human interaction
            low_city = city.lower()
            if low_city == 'chicago':
                return 'chicago.csv'
            elif low_city == 'washington':
                return 'washington.csv'
            elif low_city == 'new york':
                return 'new_york_city.csv'
            else:           #in case city is intered incorrectly
                print("\n \nNo such city is found, try entering the name of the city correctly")
        except:             #in case some error appears
            print("\n \n Some error appeared, try to enter a city name correctly")



def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) type of filter, with which we will filter the data later
    '''
    while True:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

        try:
            low_time_period = time_period.lower()
            #print(low_time_period)
            if low_time_period == 'month' or low_time_period == 'day' or low_time_period == 'none':
                #print("therefore we return: {} with a type of {}".format(low_time_period, type(low_time_period)))
                return low_time_period
                break
            else:
                print("\n\nUnknown input, please try to enter 'month' 'day' or 'none' again")
        except:
            print("Some input error must have occured")

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) month name, by which we will filter data later
    '''
    #Creating a loop to keep on asking a user for a correct input (in case, it is entered incorrectly)
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        #Trying to avoid errors that may arise from human interaction
        try:
            low_month = month.lower()
            if low_month == 'january' or low_month == 'february' or low_month == 'march' or low_month == 'april' \
            or low_month == 'may' or low_month == 'june':
                return low_month
                break
            else:
                #in case month is intered incorrectly
                print("\n \nError: No such month is found, try entering the name of the month again, correctly ")
        except:
            #in case some other errors appears
            print("\n \n Some error appeared, try to enter a city name correctly")


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        month that we want to investigate.
    Returns:
        (int) day that we want to examine
    '''
    # special characteristics of each month
    if month == "january" or month == "march" or month == "may":
        days_in_month = 31
    elif month == "february":
        days_in_month = 28
    else:
        days_in_month = 30

    #Creating a loop to keep on asking a user for a correct input (in case, it is entered incorrectly)
    while True:
        #Try to avoid errors that may arise from human interaction
        try:
            #Just a friendly reminder for a user
            print("\nP.S. it is {}, and there are {} days in {}".format(month,days_in_month,month))

            # let the user input day of interest, and translate it into an integer from a string
            day = int(input('Which day? Please type your response as an integer.\n'))
            if type(day) == int and 0<day<=days_in_month:
                return day
                break
            else:
                #in case month is intered incorrectly
                print("\n \nError: try entering correct number of days in month. Days cannot be negative, they cannot exceed numebr of days in a given month (notice that some months have - 30 days and others - 31, and February has - 28)")
        except:
            #in case some error appears or user enters non-numerical input
            print("\n \n Some error appeared, try to entering a numerical input")



def popular_month(csv_file):
    '''
    Question: What is the most popular month for start time?
    Args:
        csv_file to work with the city of the user's interest.
    Returns:
        (str) a month in which most orders were made.
    '''
    # Intitalize a list with 6 elements (each one for a single month)
    months_counter = [0]*6

    #start reading the file line-by-line and extract month during which user used the bycicle
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter=',')
        for line in data_reader:
            #extracting the number of month as an <int>
            month = int(line['Start Time'][6])

            #increment respective element in the list, to count # of orders that happend in this specific month
            months_counter[month-1] += 1

    #here we check which month was the most successeful and return its name
    number_of_popular_month = months_counter.index(max(months_counter)) + 1
    if number_of_popular_month == 1:
        return 'January'
    elif number_of_popular_month == 2:
        return 'February'
    elif number_of_popular_month == 3:
        return 'March'
    elif number_of_popular_month == 4:
        return 'April'
    elif number_of_popular_month == 5:
        return 'May'
    elif number_of_popular_month == 6:
        return 'June'
    else:
        print("some kind of error occured in POPULAR MONTH FUNCTION")

# We use this function to simplify some logistic statements
def month_into_int(month_of_interest):
    if month_of_interest == 'january':
        return(1)
    elif month_of_interest == 'february':
        return(2)
    elif month_of_interest == 'march':
        return(3)
    elif month_of_interest == 'april':
        return(4)
    elif month_of_interest == 'may':
        return(5)
    elif month_of_interest == 'june':
        return(6)


def popular_day(csv_file, month_of_interest = None):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        csv_file to work with a specified filen
        month_of_interest can be None or a month name. In case it is none, we work with the whole data set, in case it is specified month, we only work with specified one
    Returns:
        (str) name of the week day that had most bike rides registered
    '''

    days_counter = [0]*7  #quite specific, we have 7 days a week
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter=',')       #open a file to work
        for line in data_reader:                                # start reading data by line
            #print("it is month {}".format(line['Start Time'][6]))
            if month_of_interest == None:
                year = int(line['Start Time'][0:4])
                month = int(line['Start Time'][6])
                day = int(line['Start Time'][8:10])

                #we translate it into a day of week (0,1...6) using weekday() funciton
                it_is = date(year, month, day).weekday()
                #print('program entered everything')
                days_counter[it_is] += 1
            # if user wants monthly data, we extract only relevant data for that month
            elif  int(line['Start Time'][6]) == month_into_int(month_of_interest):
                year = int(line['Start Time'][0:4])     #extracts year
                month = int(line['Start Time'][6])      #extracts month
                day = int(line['Start Time'][8:10])     #excracts day

                #we translate it into a day of week (0,1...6) using weekday() funciton
                it_is = date(year, month, day).weekday()
                #increment each day of week in a list
                days_counter[it_is] += 1

    #understanding which day in the list had most orders
    number_of_popular_day = days_counter.index(max(days_counter))
    #returning relevant day
    if number_of_popular_day == 0:
        return'Monday'
    elif number_of_popular_day == 1:
        return'Tuesday'
    elif number_of_popular_day == 2:
        return 'Wednsday'
    elif number_of_popular_day == 3:
        return 'Thursday'
    elif number_of_popular_day == 4:
        return 'Friday'
    elif number_of_popular_day == 5:
        return 'Saturday'
    elif number_of_popular_day == 6:
        return'Sunday'


def popular_hour(csv_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What is the most popular hour of day for start time?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (int) number of hour that had the most bicycle rides registered
    '''
    # create a list for each of 24 hour slots to increment later
    hours_counter = [0]*24

    # start reading data by line
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter=',')
        for line in data_reader:

            # if we want monthly data
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:
                    # extracting the hour of interest
                    hour_of_interest = int(line['Start Time'][11:13])
                    hours_counter[hour_of_interest] += 1
                    # line below was used to debug
                    #print("currently hours counter is: {}".format(hours_counter))
            # if we want daily data
            elif time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:
                    # extracting the hour of interest
                    hour_of_interest = int(line['Start Time'][11:13])
                    hours_counter[hour_of_interest] += 1
                    # line below was used to debug
                    #print("currently hours counter is: {}".format(hours_counter))
            # all other cases
            elif time_period == 'none':
                # extracting the hour of interest
                hour_of_interest = int(line['Start Time'][11:13])
                hours_counter[hour_of_interest] += 1
                # line below was used to debug
                #print("currently hours counter is: {}".format(hours_counter))
    most_popular_hour = hours_counter.index(max(hours_counter))
    return most_popular_hour


def trip_duration(csv_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What is the total trip duration and average trip duration?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (int, float): total duration of all trips (in seconds), average duration of trips (in seconds)
    '''
    # create a format template
    FMT = '%H:%M:%S'

    # initializing variables the we will need
    initial_time = 0
    total_trip = 0
    average_trip = 0
    number_of_trips = 0

    # starting to read the data line by line
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter=',')
        for line in data_reader:

            # in case we sorting by month
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:
                    # extracting start and end time
                    t1 = (line['Start Time'][11:19])
                    t2 = (line['End Time'][11:19])

                    # converting start and end time to datetime type
                    t1_datetime = datetime.strptime(t1, FMT)
                    t2_datetime = datetime.strptime(t2, FMT)

                    #finding the difference between 2 times in
                    tdelta = t2_datetime - t1_datetime
                    tdelta_in_seconds = tdelta.seconds
                    total_trip += tdelta_in_seconds
                    number_of_trips += 1

            # in case we sorting by day
            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:
                    # extracting start and end time
                    t1 = (line['Start Time'][11:19])
                    t2 = (line['End Time'][11:19])

                    # converting start and end time to datetime type
                    t1_datetime = datetime.strptime(t1, FMT)
                    t2_datetime = datetime.strptime(t2, FMT)

                    #finding the difference between 2 times in
                    tdelta = t2_datetime - t1_datetime
                    tdelta_in_seconds = tdelta.seconds
                    total_trip += tdelta_in_seconds
                    number_of_trips += 1

            if time_period == 'none':
                # extracting start and end time
                t1 = (line['Start Time'][11:19])
                t2 = (line['End Time'][11:19])

                # converting start and end time to datetime type
                t1_datetime = datetime.strptime(t1, FMT)
                t2_datetime = datetime.strptime(t2, FMT)

                #finding the difference between 2 times in
                tdelta = t2_datetime - t1_datetime
                tdelta_in_seconds = tdelta.seconds
                total_trip += tdelta_in_seconds
                number_of_trips += 1

    average_trip = total_trip /number_of_trips
    return (total_trip, average_trip)

def popular_stations(csv_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What is the most popular start station and most popular end station?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (str, int): name of the most used beginning station, and the number it has been used
        (str, int): name of the most used end station, and the number it has been used
    '''
    # initializing the dictionaries of interest
    start_stations_count = {}
    end_stations_count = {}
    # reading the respective files
    with open('new_york_city.csv', 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter = ',')
        for line in data_reader:
            # for 3 types of output, we filter data accordingly (month, day, none)
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:
                    #we extract names of stations as string type
                    current_start_station = line['Start Station']
                    current_end_station = line['End Station']

                    # here we check if the station extracted is already in the respective dictionary
                    x = start_stations_count.get(current_start_station)
                    is_null = x is None

                    # if it is not in dict, we add a station to dictionary and create a value to this key
                    if is_null:
                        start_stations_count[current_start_station] = 1
                    # if it already exist, we increment the key value
                    else:
                        start_stations_count[current_start_station] += 1

                    # same is performed for the end station
                    y = end_stations_count.get(current_end_station)
                    is_null = y is None
                    if is_null:
                        end_stations_count[current_end_station] = 1
                    else:
                        end_stations_count[current_end_station] += 1

            #similar procedures are processed for day
            elif time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:
                    current_start_station = line['Start Station']
                    current_end_station = line['End Station']

                    x = start_stations_count.get(current_start_station)
                    is_null = x is None
                    if is_null:
                        start_stations_count[current_start_station] = 1
                    else:
                        start_stations_count[current_start_station] += 1

                    y = end_stations_count.get(current_end_station)
                    is_null = y is None
                    if is_null:
                        end_stations_count[current_end_station] = 1
                    else:
                        end_stations_count[current_end_station] += 1

            # similar process if performed for none
            elif time_period == 'none':
                current_start_station = line['Start Station']
                current_end_station = line['End Station']

                x = start_stations_count.get(current_start_station)
                is_null = x is None
                if is_null:
                    start_stations_count[current_start_station] = 1
                else:
                    start_stations_count[current_start_station] += 1

                y = end_stations_count.get(current_end_station)
                is_null = y is None
                if is_null:
                    end_stations_count[current_end_station] = 1
                else:
                    end_stations_count[current_end_station] += 1

    # here we extract the most used station (start and end) and return its name and value
    max_startvalue = max(start_stations_count.values())  # maximum value
    max_startkeys = [k for k, v in start_stations_count.items() if v == max_startvalue] # getting all keys containing the `maximum`
    max_endvalue = max(end_stations_count.values())  # maximum value
    max_endkeys = [k for k, v in end_stations_count.items() if v == max_endvalue] # getting all keys containing the `maximum`
    return (max_startkeys[0], max_startvalue), (max_endkeys[0], max_endvalue)


def popular_trip(csv_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What is the most popular trip?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (tuple) most popular trip taken (with 1st variable as a start station, and 2nd as an end station)
    '''
    # initialize dictionary of trips
    trips_count = {}

    # starting to read the data line by line
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter=',')
        for line in data_reader:

            # for 3 types of output, we filter data accordingly (month, day, none)
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:

                    #extracting start and end stations
                    current_start_station = line['Start Station']
                    current_end_station = line['End Station']

                    #combining them into one single trip of type tuple
                    current_trip = (current_start_station, current_end_station)
                    #print(current_trip, type(current_trip))

                    #checking if this trip is already in the dictionary
                    x = trips_count.get(current_trip)
                    is_null = x is None
                    if is_null:
                        #if it is not, we add this trip to a dictionary
                        trips_count[current_trip] = 1
                    else:
                        #if it is already in dict, we increment the ammount of times this trip had been taken
                        trips_count[current_trip] += 1

            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:

                    #extracting start and end stations
                    current_start_station = line['Start Station']
                    current_end_station = line['End Station']

                    #combining them into one single trip of type tuple
                    current_trip = (current_start_station, current_end_station)
                    #print(current_trip, type(current_trip))

                    #checking if this trip is already in the dictionary
                    x = trips_count.get(current_trip)
                    is_null = x is None
                    if is_null:
                        #if it is not, we add this trip to a dictionary
                        trips_count[current_trip] = 1
                    else:
                        #if it is already in dict, we increment the ammount of times this trip had been taken
                        trips_count[current_trip] += 1

            if time_period == 'none':
                current_start_station = line['Start Station']
                current_end_station = line['End Station']

                current_trip = (current_start_station, current_end_station)
                #print(current_trip, type(current_trip))

                x = trips_count.get(current_trip)
                is_null = x is None
                if is_null:
                    trips_count[current_trip] = 1
                else:
                    trips_count[current_trip] += 1

    # here we extract the most used trip and return its name and value
    max_tripvalue = max(trips_count.values())  # maximum value
    max_tripkeys = [k for k, v in trips_count.items() if v == max_tripvalue] # getting all keys containing the `maximum`
    return(max_tripkeys[0])

def users(csv_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What are the counts of each user type?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (dictionary) of types of user types and the respective ammount in each category
    '''
    #initializing dictionary of user types
    user_types = {}

    # open the file and start reading it line-by-line
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter = ',')
        for line in data_reader:

            # for each 3 types of sorting data
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:

                    # we extract the types of users that we have
                    current_user = line['User Type']

                    #here we check if this particular type of user is already in the dictionary
                    x = user_types.get(current_user)
                    is_null = x is None

                    if is_null:
                        # if it is not in the dict, we add a user type to dict and start a counter
                        user_types[current_user] = 1
                    else:
                        # if it already exist, we increment the value
                        user_types[current_user] += 1

            #similar procedure is performed for the daily sorting
            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:                    # we extract the types of users that we have
                    current_user = line['User Type']
                    x = user_types.get(current_user)
                    is_null = x is None
                    if is_null:
                        user_types[current_user] = 1
                    else:
                        user_types[current_user] += 1

            # similar process if performed for none
            elif time_period == 'none':
                current_user = line['User Type']
                x = user_types.get(current_user)
                is_null = x is None
                if is_null:
                    user_types[current_user] = 1
                else:
                    user_types[current_user] += 1
    return user_types


def gender(csv_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What are the counts of gender?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (dictionary) of genders
    '''
    #initializing genders dictionary
    gender_types = {}

    # open the file of interest and start reading it
    with open(csv_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter = ',')
        for line in data_reader:

            # for each 3 types of sorting data
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:

                    # we extract the types of users that we have
                    current_gender = line['Gender']

                    #here we check if this particular type of user is already in the dictionary
                    x = gender_types.get(current_gender)
                    is_null = x is None

                    # if it is not in the dict, we add a user type to dict and start a counter
                    if is_null:
                        gender_types[current_gender] = 1
                    # if it already exist, we increment the value
                    else:
                        gender_types[current_gender] += 1

            #similar procedure is performed for the daily sorting
            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:                    # we extract the types of users that we have
                    current_gender = line['Gender']
                    x = gender_types.get(current_gender)
                    is_null = x is None
                    if is_null:
                        gender_types[current_gender] = 1
                    else:
                        gender_types[current_gender] += 1

            # similar process if performed for none
            elif time_period == 'none':
                current_gender = line['Gender']
                x = gender_types.get(current_gender)
                is_null = x is None
                if is_null:
                    gender_types[current_gender] = 1
                else:
                    gender_types[current_gender] += 1
    return gender_types



# HALF ASSED WORK, SEEMS TO WORK BUT NEED TO TIE IT INTO THE WHOLE SYSTEM
def birth_years(city_file, time_period, month_of_interest = None, day_of_interest = None):
    '''
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Args:
        csv_file: specifies the document with the file of day_of_interest
        time_period: specifies if we are interested in overall data, month-specific or day-specific
        month_of_interest: if time_period is none, then this statement must be also 'none', otherwise it indicates the month of our interest
        day_of_interest: used only if time_period is 'day', otherwise must be an empty statement
    Returns:
        (int, int, int): the average age of a user, the minimal age of a user, the maximal age of a user.
    '''
    #initializing dictionary of birth_years
    birth_years = {}

    # open the file of interest and start reading it
    with open(city_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter = ',')
        for line in data_reader:

            # for each 3 types of sorting data
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:

                    # we avoid empty input, using this if statement
                    if line['Birth Year'] != '':

                        # extracting birthday and callculating age
                        current_age = 2017 - int(float((line['Birth Year'])))
                        #print(current_age)

                        #here we check if this particular type of user is already in the dictionary
                        x = birth_years.get(current_age)
                        is_null = x is None
                            # if it is not in the dict, we add this age to dict and start a counter
                        if is_null:
                            birth_years[current_age] = 1
                                # if it already exist, we increment the value
                        else:
                            birth_years[current_age] += 1

            #similar procedure is performed for the daily sorting
            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:                    # we extract the types of users that we have
                    if line['Birth Year'] != '':
                        current_age = 2017 - int(float((line['Birth Year'])))
                        #print(current_age)
                        x = birth_years.get(current_age)
                        is_null = x is None
                        if is_null:
                            birth_years[current_age] = 1
                        else:
                            birth_years[current_age] += 1

            # similar process if performed for none
            elif time_period == 'none':
                if line['Birth Year'] != '':
                    current_age = 2017 - int(float((line['Birth Year'])))
                    #print(current_age)
                    x = birth_years.get(current_age)
                    is_null = x is None
                    if is_null:
                        birth_years[current_age] = 1
                    else:
                        birth_years[current_age] += 1
    # extracting the most common age of users
    max_birthvalue = max(birth_years.values())  # maximum value
    max_birthkeys = [k for k, v in birth_years.items() if v == max_birthvalue] # getting all keys containing the `maximum`

    # initializing lists, and counters
    extract_keys = list(birth_years)
    i = 0
    birthday_keys = []
    # extracting each of the keys as integet into a new list
    for element in extract_keys:
        birthday_keys.append(int(element))
    # finding the youngest and oldest ages
    earliest_person = min(birthday_keys)
    oldest_person = max(birthday_keys)
    return max_birthkeys[0], earliest_person, oldest_person

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

    while True:
          answer = input('\nWould you like to view 5 more individual trip datas? Type \'yes\' or \'no\'.\n')
          #Trying to avoid errors that may arise from human interaction
          try:
              low_display = answer.lower()
              if low_display == 'yes' or low_display == 'no':
                  #return low_month
                  break
              else:
                  #in case month is intered incorrectly
                  print("\n \nError: Invalid input, try entering yes or no correctly ")
          except:
              #in case some other errors appears
              print("\n \n Some error appeared, try to enter yes or no  correctly")



    if low_display == 'yes':
        #print('fuction correctly enters this statement')
        display_data(csv_file, n+1)



def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)

    #ask user to input a city of interest
    city_file = get_city()

    #based on the user's interest refer city_file to the city file of interest
    #if city == 'Chicago':
    #    city_file = chicago
    #elif city == 'New York':
    #    city_file = new_york_city
    #elif city == 'Washington':
    #    city_file = washington

    # Filter by time period (month, day, none)

    #create empty strings for month of interst and day of interest, ask user to specify how we want to sort the data
    month_of_interest = None
    day_of_interest = None
    time_period = get_time_period()

    #based on how user wants to sort the data, ask him to add month and day of interest if necessery
    if time_period == 'month':
        month_of_interest = get_month()
        #print("here my month of interest is: {}".format(month_of_interest))
    elif time_period == 'day':
        #notice that get_month returns a <str> and get_day returns an <int>
        month_of_interest = get_month()
        day_of_interest = get_day(month_of_interest)


    print('\n\nCalculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        peak_month = popular_month(city_file)
        print("\nThe most popular month for a bike ride is: {}".format(peak_month))
        print("That took %s seconds.\n" % (time.time() - start_time))

        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        peak_day = popular_day(city_file, month_of_interest)
        print("\n\nThe most popular day for a bike ride is: {}".format(peak_day))
        print("That took %s seconds.\n" % (time.time() - start_time))

        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    peak_hour = popular_hour(city_file, time_period, month_of_interest, day_of_interest)
    print("\n\nThe most popular hour for a bike ride is : {}\n".format(peak_hour))
    print("That took %s seconds.\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?

    total_duration, average_duration = trip_duration(city_file, time_period, month_of_interest, day_of_interest)
    print("\n\nThe total bicycle trip duration (in seconds) is: {}. The average bycicle trip duration (in seconds) is: {}\n".format(total_duration, average_duration))
    print("That took %s seconds.\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?

    (pop_start_stn, number_pop_start), (pop_end_stn, number_pop_end) = popular_stations(city_file, time_period, month_of_interest, day_of_interest)
    print("\n\nThe most popular start station is: {}\nand the most popular end station is: {}\n".format(pop_start_stn, pop_end_stn))
    print("That took %s seconds.\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    most_popular_trip = popular_trip(city_file, time_period, month_of_interest, day_of_interest)
    print("\n\nThe most popular trip is {}\n".format(most_popular_trip))
    print("That took %s seconds.\n" % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    counts_of_types = users(city_file, time_period, month_of_interest, day_of_interest)
    print("\n\nHere you can see two category of users, and the respective ammount of users in each category \n{}\n".format(counts_of_types))
    print("That took %s seconds.\n" % (time.time() - start_time))

    if city_file != 'washington.csv':
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?

        genders = gender(city_file, time_period, month_of_interest, day_of_interest)
        print("\n\nHere you can see ammount of male and female users (and also those who do not specify their gender): \n{}\n".format(genders))
        print("That took %s seconds.\n" % (time.time() - start_time))


        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        average_age, minimal_age, maximal_age = birth_years(city_file, time_period, month_of_interest, day_of_interest)
        print("\n\nAvergae age of a user is: {}\n".format(average_age))
        print("Minimal and maximal age of a users are: {} & {}\n".format(minimal_age, maximal_age))
        print("That took %s seconds.\n" % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    while True:
          restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
          #Trying to avoid errors that may arise from human interaction
          try:
              low_restart = restart.lower()
              if low_restart == 'yes' or low_restart == 'no':
                  break
              else:
                  #in case month is intered incorrectly
                  print("\n \nError: Invalid input, try entering yes or no correctly ")
          except:
              #in case some other errors appears
              print("\n \n Some error appeared, try to enter a yes or no correctly")

    print("here low restart equals to {}".format(low_restart))
    if low_restart == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()

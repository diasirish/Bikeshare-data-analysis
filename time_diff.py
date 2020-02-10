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

def trip_duration(city_file, time_period, month_of_interest = None, day_of_interest = None):
    FMT = '%H:%M:%S'
    initial_time = 0
    total_trip = 0
    average_trip = 0
    number_of_trips = 0
    with open(city_file, 'r') as f_in:
        data_reader = csv.DictReader(f_in, delimiter=',')
        for line in data_reader:
            if time_period == 'month':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month:
                    t1 = (line['Start Time'][11:19])
                    t2 = (line['End Time'][11:19])
                    print(t1, t2, type(t1))
                    t1_datetime = datetime.strptime(t1, FMT)
                    t2_datetime = datetime.strptime(t2, FMT)
                    print(t1_datetime, t2_datetime, type(t1_datetime))
                    tdelta = t2_datetime - t1_datetime
                    tdelta_in_seconds = tdelta.seconds
                    print(tdelta, type(tdelta))
                    print('it must be in seconds: {} and it is type {}'.format(tdelta_in_seconds, type(tdelta_in_seconds)))
                    total_trip += tdelta_in_seconds
                    number_of_trips += 1
                    print('program got here: TIME PERIOD: Month, total_trip : {}'.format(total_trip))
            if time_period == 'day':
                number_of_month = month_into_int(month_of_interest)
                if int(line['Start Time'][6]) == number_of_month and int(line['Start Time'][8:10]) == day_of_interest:
                    t1 = (line['Start Time'][11:19])
                    t2 = (line['End Time'][11:19])
                    print(t1, t2, type(t1))
                    t1_datetime = datetime.strptime(t1, FMT)
                    t2_datetime = datetime.strptime(t2, FMT)
                    print(t1_datetime, t2_datetime, type(t1_datetime))
                    tdelta = t2_datetime - t1_datetime
                    tdelta_in_seconds = tdelta.seconds
                    print(tdelta, type(tdelta))
                    print('it must be in seconds: {} and it is type {}'.format(tdelta_in_seconds, type(tdelta_in_seconds)))
                    total_trip += tdelta_in_seconds
                    number_of_trips += 1
                    print('program got here: TIME PERIOD: Day, total_trip : {}'.format(total_trip))
            if time_period == 'none':
                t1 = (line['Start Time'][11:19])
                t2 = (line['End Time'][11:19])
                print(t1, t2, type(t1))
                t1_datetime = datetime.strptime(t1, FMT)
                t2_datetime = datetime.strptime(t2, FMT)
                print(t1_datetime, t2_datetime, type(t1_datetime))
                tdelta = t2_datetime - t1_datetime
                tdelta_in_seconds = tdelta.seconds
                print(tdelta, type(tdelta))
                print('it must be in seconds: {} and it is type {}'.format(tdelta_in_seconds, type(tdelta_in_seconds)))
                total_trip += tdelta_in_seconds
                number_of_trips += 1
                print('program got here: TIME PERIOD: NONE, total_trip : {}'.format(total_trip))
    average_trip = total_trip /number_of_trips
    return (total_trip, average_trip)

(extract_total, extract_average) = trip_duration('chicago.csv', 'month', 'January')
print(extract_total)
print(extract_average)

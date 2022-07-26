# the extra resources used
#https://github.com/Aritra96
#https://stackoverflow.com/questions/23294658
#https://classroom.udacity.com/nanodegrees/nd104/parts/cd0024/modules/1e4392d9-c759-42d1-8204-aaed736ae199/lessons/ls1727/concepts/ff725dae-97d7-4d8d-ab8b-9ca18c89aa48
#https://classroom.udacity.com/nanodegrees/nd104/parts/cd0024/modules/1e4392d9-c759-42d1-8204-aaed736ae199/lessons/ls1727/concepts/7a33cce4-18de-48a4-8aeb-d0c13c972909

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Holla! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''
    # Running this loop to ensure the correct user input gets selected else repeat
    while city not in CITY_DATA.keys():
        print("\nKindly select your preferred city:")
        print("\nPlease choose as written from (Chicago, New York City, Washington). \nNote: Don\'t worry the city name is not case sensitive.")
        # user input converted to lower to standardize them
        
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nThat was\'nt a correct input, kindly select from (Chicago, New York City, Washington). \nNote: Don\'t worry the city name is not case sensitive.")
            time.sleep(1.5)
    print("\nCongrats! you just selected {} as your preferred city.".format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    # Creating a dictionary to store all the months including the 'all' option
    MONTH = {'january': 1, 'february': 2, 'march': 3,
                  'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH.keys():
        print("\nKindly select your preffered month, from January to June:")
        print("Kindly enter in the month like this: january, february, march, april, may, june or all if you can\'t seem to choose, \nNote: Don\'t worry the month name is not case sensitive.")
        month = input().lower()

        if month not in MONTH.keys():
            print("\nThat was\'nt a correct input. Could you maybe try selecting a month like this:january, february, march, april, may, june or all if you can\'t seem to choose. \nNote: month name is not case sensitive.")
            time.sleep(1.5)
            
    print("\nYippe! Great job! Your selected month of interest is: {}.".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Creating a list to store all the days including the 'all' option
    DAY = ['all', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY:
        print("\nIt\'s time to select your preferred day:")
        print("Kindly enter your preferred day like this: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all if you can\'t seem to choose.\nNote: day of interest is not case sensitive.")
        day = input().lower()

        if day not in DAY:
            print("\nOopsie that was a wrong input. Kindly enter your preferred day like this: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all if you can\'t seem to choose. \nNote: day of interest is not case sensitive.")
            time.sleep(1.5)
            
    print("\nYay! you just selected: {}.".format(day.title()))
    print("\nNow let\'s both explore data for city: {}, month/s: {} and day/s: {}.".format(city.upper(), month.upper(), day.upper()))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nGimme a moment ...")
    df = pd.read_csv(CITY_DATA[city])
    
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    common_month = df['month'].mode()[0]
    print(f"\nMost common month: {common_month}")
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"\nMost Common Day of the week: {common_day}")

  

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print(f"\nMost common Start Hour: {hour}")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nI\'m calculating The Most Popular Stations and Trip, gimme a min...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {start_station}")

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    ss_es = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of trips are from {ss_es}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)

    print(f"The total travel time is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)

    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average travel time is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average travel time is {mins} minutes and {sec} seconds.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user = df['User Type'].value_counts()
    print("The counts of users types are given below:\n\n{}".format(user))

    # TO DO: Display counts of gender
    print('\n Collating Gender stats......')
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe user gender are given below:\n\n{gender}")
    except:
        print("\nThis city has no 'Gender' column.")

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\n Collating Birth Year stats......')
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("\nThis city has no information about the year of birth of users.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

#Function to display the data frame itself as per user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.

    Args:
        param1 (df): The data frame we are working with.

    Returns:
        None.
    """
    RESPONSE_LIST = ['yes', 'no']
    view_data = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while view_data not in RESPONSE_LIST:
        print("\nDo you want to view the raw data?")
        print("\nYour response should be:\nYes or yes\nNo or no")
        view_data = input().lower()
        #the raw data from the df is displayed if user opts for it
        if view_data == "yes":
            print(df.head())
        elif view_data not in RESPONSE_LIST:
            print("\Your response wasn\'t correct.")
            print("it has to be yes or no.")
            

    #Extra while loop here to ask user if they want to continue viewing data
    while view_data == 'yes':
        print("Do you want to see more raw data?")
        counter += 5
        view_data = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if view_data == "yes":
             print(df[counter:counter+5])
        elif view_data != "yes":
             break

    print('-'*40)
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nThat was fun! wanna go again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
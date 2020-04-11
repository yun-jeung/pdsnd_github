
# updated: 16.03.2020
# This script was uploaded in GitHub, 11.04.2020
import time
import pandas as pd
import numpy as np

# Define Deictinaries or Lists
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
"""
csv title
Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year

"""

MONTH_LIST = ['january', 'february',
              'march','april','may',
              'june', 'all']

DAY_LIST = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday',
            'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('------- Hello! Let\'s explore some US bikeshare data!------')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        city = input("\nWhich city you would like to fiter? Choose from "
                     "New York City, Chicago, and Washington.\n").lower()

        if city not in CITY_DATA.keys():
            print("\n Pleasce check your spelling or not in the list.")

        print(f"\n>>>>Check you chose {city.title()}.")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in MONTH_LIST:
        month = input("\nWhich month you would like to fiter? Choose from "
                     "January to June, or All.\n").lower()

        if month not in MONTH_LIST:
            print("\n Pleasce check your spelling or not in the list.")

        print(f"\n>>>>Check you chose {month.title()}.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        # TO DO: get user input for month (all, january, february, ... , june)
    day = ''
    while day not in DAY_LIST:
        day = input("\nWhich day you would like to fiter? Choose from "
                     "Monday to Sunday, or All.\n").lower()

        if day not in DAY_LIST:
            print("\n Pleasce check your spelling or not in the list.")

        print(f"\n>>>> Check you chose {day.title()}.")

    print('-'*60)
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
    print("\n.... Loding data ....")
    # Reading city data
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month
    if month != 'all':
        month = MONTH_LIST.index(month) + 1
        # print("..test ...", month)

        # Filter by MONTH to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # Filter by DAY to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n.... Calculating The Most Frequent Times of Travel ....\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print(f"\nThe most popular month is {popular_month}")

    # TO DO: display the most common day of week
    popular_day =df['day_of_week'].mode()[0]

    print(f"\nThe most popular day is {popular_day}")

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0] # showing 24 hours
    #!!! Might be good to show as 12 hours and am/pm #
    print(f"\nThe most popular hour is {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n.... Calculating The Most Popular Stations and Trip ....\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print(f"\n{common_start_station} is the most commonly used start station.")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print(f"\n{common_end_station} is the most commonly used end station.")

    # TO DO: display most frequent combination of start station and end station trip
    # frequent_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
    # print(f"The most frequent trip is {frequent_trip}")
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep =' to ')
    frequent_trip = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {frequent_trip}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n.... Calculating Trip Duration ....\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    # Convert time into hours, minutes, and seconds
    minute, second = divmod(total_travel_time, 60)
    #print('TEST......',divmod(total_travel_time, 60))
    hour, minute = divmod(minute, 60)

    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")


    # TO DO: display mean travel time
    # Calculating the average trip duration using mean method
    avergage_trip_duration = round(df['Trip Duration'].mean())
    # Convert time into hours, minutes, and seconds
    mins, sec = divmod(average_trip_duration, 60)
    # This filter prints the time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n... Calculating User Stats ...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    #print('TEST.....',user_type)
    print(f"\nThe user types are:\n{user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users sorted by gender:\n{gender}")
    except:
        print("\nThere is no coloumn sorted by Gender in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        #print(f"The earliest year is:\n{earliest}")
        most_recent = df['Birth Year'].max()
        #print(f"The earliest year is:\n{most_recent}")
        most_common_year = df['Birth Year'].mode()[0]
        #print("The earliest year is:\n",int(most_common_year))

        print("\nThe earliest year of birth: ", int(earliest),
              "\nThe youngest year of birth: ", int(most_recent),
              "\nThe most common year of birth: ", int(most_common_year))

    except KeyError:
        print("\nThere is NO data available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

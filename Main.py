# Name: Donald Azevedo
# Student ID: 011371173
# Class: C950 Data Structures and Algorithms II

import datetime
import sys
from builtins import ValueError

from Tools.PackageManager import PackageManager
from Tools.AddressManager import AddressManager
from Tools.DispatchManager import DispatchManager
from Tools.ReportGenerator import ReportGenerator

from Classes.Truck import Truck

# Instantiating PackageManager, providing packages directory
# This object utilizes the hashtable data structure and provides an interface
package_manager = PackageManager("CSV_Files/Packages.csv")


# Instantiating AddressManager, Providing needed directories
# This object serves as an abstraction to useful address information processing
address_manager = AddressManager("CSV_Files/Addresses.csv", "CSV_Files/Distances.csv")


# Instantiating DispatchManager
# It utilizes AddressManager and PackageManager for dispatching trucks
dispatch_manager = DispatchManager(package_manager, address_manager)


# Instantiating ReportGenerator
# This is a tool for generating reports related to the parcel service
report_generator = ReportGenerator(package_manager, address_manager)



# Manually "Loading" the trucks with packages via class constructor instantiation:

# Truck 1 (High Priority truck)
truck1 = Truck(1, 16, [1, 13, 14, 15, 19, 16, 20, 29, 30, 31, 34, 37, 40], 18, 0.0,
               "4001 South 700 East", datetime.timedelta(hours=8))

# Truck 2 (Standard Priority truck)
truck2 = Truck(2, 16, [3, 9, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 18, 0.0,
               "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Truck 3 (Express Priority Truck)
truck3 = Truck(3, 16, [2, 4, 5, 6, 7, 8, 12, 10, 11, 25, 28, 32, 33], 18, 0.0,
               "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

#Dispatching Truck 1
dispatch_manager.dispatch(truck1)

#Dispatching Truck 3
dispatch_manager.dispatch(truck3)

#Dispatching Truck 2
dispatch_manager.dispatch(truck2)

## Begin CLI Program

print("=== WGUPS Delivery Lookup Service ===")
# Generating loop for program interface
while True:
    # Main menu with several selections
    print("=== Main Menu ===")
    print("Please select an option:")
    print("1: Get total miles traveled")
    print("2: Get package status at specific time")
    print("3: Get a full package report at a specific time")
    print("4: Exit")

    # Waiting for user input
    user_input = input("Enter your selection: ")


    #Processing input for total miles
    if user_input == '1':
        report_generator.get_total_miles(truck1, truck2, truck3)


    #Processing input for specific package
    elif user_input == '2':
        #Requesting input for Package ID
        while True:
            try:
                pid = int(input("Please enter a package ID#: "))
                break  # Break out of the loop if input is successfully converted to an integer
            except ValueError:
                print("Invalid input. Please enter an integer for the package ID.")
        # Requesting input for time Hours then Minutes
        print("You will now need to enter the hour and minutes of the time for the package status ")
        while True:
            try:
                hours = int(input("Enter the hour (0-23): "))
                if hours < 0 or hours > 23:
                    raise ValueError("Hours must be between 0 and 23")
                break  # Break out of the loop if input is successfully converted to an integer and within range
            except ValueError as e:
                print(e)

        while True:
            try:
                minutes = int(input("Enter the minutes (0-59): "))
                if minutes < 0 or minutes > 59:
                    raise ValueError("Minutes must be between 0 and 59")
                break  # Break out of the loop if input is successfully converted to an integer and within range
            except ValueError as e:
                print(e)

        # Create a timedelta object using the provided hours and minutes
        time = datetime.timedelta(hours=hours, minutes=minutes)

        report_generator.get_package_status(pid, time)

    # Processing Input for a full report
    elif user_input == '3':
        print("You will now need to enter the hour and minutes of the time for full package report ")
        while True:
            try:
                hours = int(input("Enter the hour (0-23): "))
                if hours < 0 or hours > 23:
                    raise ValueError("Hours must be between 0 and 23")
                break  # Break out of the loop if input is successfully converted to an integer and within range
            except ValueError as e:
                print(e)

        while True:
            try:
                minutes = int(input("Enter the minutes (0-59): "))
                if minutes < 0 or minutes > 59:
                    raise ValueError("Minutes must be between 0 and 59")
                break  # Break out of the loop if input is successfully converted to an integer and within range
            except ValueError as e:
                print(e)

        # Create a timedelta object using the provided hours and minutes
        time = datetime.timedelta(hours=hours, minutes=minutes)
        # Running the report with the needed information
        report_generator.full_report(time)


    #Processing input for exiting
    elif user_input == '4':
        print("Exiting program. Goodbye!")
        sys.exit()

    #Processing invalid input
    else:
        print("Invalid input. Please enter a valid option.")

    #Allowing the user to view the data before proceeding
    input("Press Enter to continue...")
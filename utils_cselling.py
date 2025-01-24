"""
Module: utils_cselling

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for Module P1. 
This program calculates several statistic functions for client turnaround time.
YIPPEEEEE!!!!!

Author: Caleb Sellinger

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""
# Updated description and byline for Final Iteration

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics   # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True
is_in_unitedstates: bool = True
is_in_unitedstates = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 10
number_of_clients: int = 4

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.7
average_num_clients: float = 3.42

# declare a list of strings
# TODO: Add or replace this with your own list  
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
clients: list = ["Client 1", "Client 2", "Client 3","Client 4"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
client_turnaround_time: list = [431, 324, 874, 512] # in days

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_turnaround: float = min(client_turnaround_time)  
max_turnaround: float = max(client_turnaround_time)  
mean_turnaround: float = statistics.mean(client_turnaround_time)  
stdev_score: float = statistics.stdev(client_turnaround_time)

# Accidentally updated vars in iter4. Adding an additional stat for median high and low below
# Comment for iter5
median_high: float = statistics.median_high(client_turnaround_time)
median_low: float = statistics.median_low(client_turnaround_time)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Jorq's Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {is_in_unitedstates}
Years in Operation:         {number_of_clients}
Skills Offered:             {clients}
Client Client Turnaround Times: {client_satisfaction_scores}
Minimum Client Turnaround Time: {min_turnaround}
Maximum Client Turnaround Time: {max_turnaround}
Mean Client Turnaround Time: {mean_turnaround:.2f}
Standard Deviation of client turnaround time: {stdev_score:.2f}
Median High Client Turnaround Time: {median_high}
Median Low Client Turnaround Time: {median_low}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
#Author : Katlego

"""
A module-level docstring is a string literal placed at the very top of a Python module file (before any code or imports) to explain its overarching purpose, contents, and usage.
"""


def calculate_average(num1,num2,num3,num4,num5):

    """
    This function takes five numbers and calculate the average
    Parameter (number 1 to 5)-> numbers to add and get the average
    return average -> calculated average
     """
    average = num1+num2+num3+num4+num5 / 5

    return average


def format_currency(amount):

    """
    This function takes the calculated average and then format it to Rand
    parameter amount -> the amount to format
    return -> formatted amount in rand
    """
    
    return "R" + format(amount, ",.2f")


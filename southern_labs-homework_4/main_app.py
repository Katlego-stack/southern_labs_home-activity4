#Author : Katlego

import random
import datetime
import data_utils

def main():

    num1 = random.randint(50, 100)
    num2 = random.randint(50, 100)
    num3 = random.randint(50, 100)
    num4 = random.randint(50, 100)
    num5 = random.randint(50, 100)

    print(datetime.date.today())

    average = data_utils.calculate_average(num1,num2,num3,num4,num5)
    formatted_average = data_utils.format_currency(average)

    print(formatted_average)

if __name__ == "__main__":
    main()


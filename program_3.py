# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

#Author: Faith Lamah
#Date: 09/24/2025
#Title: Average Rainfall

def main():
    ######################
    year = int(input('How many years of rainfall would you like collected? '))
    total_rainfall = 0
    for x in range(year):
        for month in range(1, 13):
            month_rainfall = int(input(f'How many inches of rainfall was in month {month}?'))
            month = month + 1
            total_rainfall = total_rainfall + month_rainfall
    print(f'The total rainfall is {total_rainfall} inches.')
    print(f'The total number of months is {month - 1}.')
    print(f'The average rainfall per month for the entire period is {total_rainfall/month} inches.')
    ######################    


if __name__ == '__main__':
    main()
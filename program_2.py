# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

#Author: Faith Lamah
#Date: 09/24/2025
#Title: Movie Tix

def main():
    ######################
    total = 0.0
    another_movie = 'yes'
    while another_movie == 'yes':
        input('What movie are you watching? ')
        tickets = int(input('How many tickets do you need? '))
        total = total + tickets
        print(f'The total number of tickets is {total}')
        another_movie = input('Would you like to watch another movie? (enter "yes" if yes) ')



    ######################


if __name__ == '__main__':
    main()
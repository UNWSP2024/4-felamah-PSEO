# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    spent = 1.0         #initialize for while loop
    total = 0.0
    another_expense = 'yes'
    budget = int(input('What is the amount that you have budgeted for the month?'))
    while another_expense == 'Yes' or another_expense == 'yes':
        expense = int(input('How much is this expense?'))
        total = total + expense
        print(f'The total expense is ${total}.')
        another_expense = input('Do you have another expense? (enter "0" for no)')

        if total > budget:
            print(f'You are over the budget by ${total - budget}.')
        elif total < budget:
            print(f'You are under the budget by ${budget - total}.')
        else:
            print('You have spent exactly your budget!')



if __name__ == '__main__':
    main()
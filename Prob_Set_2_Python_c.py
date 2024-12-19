# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Establish Variables and input requests
print('Enter the starting salary:')
starting_salary=float(input())
#Initializing another starting salary variable equal to the orignal input so that we can reset the variable after each iteration
starting_salary1=starting_salary

#Initializing more variables
total_cost=1000000
portion_down_payment=.25*total_cost
months= 0
current_savings= 0
r=.04
semi_annual_raise=.07
high=10000
low=0
num_guess=0

#Execute the following while loop until one of either conditions (with break) are met. 
while True:
    #If the difference between current savings and downpayment is less than the acceptable range (+- 100), execute a guess into current savings
    if current_savings-portion_down_payment<-100:
        guess=(high+low)//2.0
        current_savings += current_savings*r/12
        current_savings += (guess/10000.0)*(starting_salary/12)
        months+=1
        #If months is divisible by six, add the semi-annual raise to the starting salary  
        if months % 6 == 0:
            starting_salary += semi_annual_raise*starting_salary
        #If months exceeds 36 and current savings has not yet gotten to an acceptable range: change the low bound to be equal to the guess, add a guess, and reset values   
        if months>36 and current_savings-portion_down_payment<-100:
            low=guess
            current_savings=0
            starting_salary=starting_salary1
            num_guess += 1
            months=0
        #If the inputed salary is too low to be able to save for the down payment, print and break
        if guess-10000>=-1 and current_savings-portion_down_payment<-100:
            print('It is not possible to pay the down payment in three years.')
            break
        #Otherwise, if the difference between current savings and down payment exceeds the acceptable range: change the high bound to be equal to guess, add a guess, and reset values 
        elif current_savings-portion_down_payment>100:
            high=guess
            current_savings=0
            starting_salary=starting_salary1
            num_guess += 1
            months=0
        #Otherwise, if the difference between current savings and down payment reaches the acceptable range: print the accepted savings rate, print the number of guesses in the search
        elif current_savings-portion_down_payment<=100 and current_savings-portion_down_payment>=-100:
            print('Best savings rate:'+ str(guess/10000.0))
            print('Steps in bisection search:' + str(num_guess))
            break
        



      



 










import math

# a program to calculate either interest on investment or the amount you pay monthly on a home loan
# we will first ask user which of the 2 above they would like to calculate
print("""investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan""") 
user_input = input("choose either investment or bond from the menu to proceed: ").lower()

if user_input == "investment":
# use conditional statements to calculate the amount including interest based on user input

    amount = int(input("please enter the amount of money you are depositing: "))
    interest_percentage = input("please enter the interest rate as a percentage: ")
    num_of_years = int(input("please enter the number of years you plan on investing for: "))
    interest = input("do you want simple or compound interest? ")
    interest_rate = int(interest_percentage) / 100
    if interest == "simple":
        total_amount = float(amount * (1 + interest_rate * num_of_years))
    else:
        total_amount = amount * math.pow((1 + interest_rate), (num_of_years))
        total_amount = round(total_amount, 2)
   
    print(total_amount)

else:
# we will assign different variables from user input to solve the equation of how much the user needs to pay per month
    value = int(input("please enter the present value of the house: "))
    interest_rate = int(input("please enter the interest rate: "))
    num_of_month = int(input("please enter the number of months you plan on repaying the bond: "))
    monthly_interest_rate = float(interest_rate / 12)
    pay_per_month = (monthly_interest_rate * value)/(1-(1 + monthly_interest_rate)**(-num_of_month))
    pay_per_month = round(pay_per_month, 2)
    print(pay_per_month)
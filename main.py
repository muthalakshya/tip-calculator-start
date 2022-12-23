#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

print("Welcome to the tip calculator!")

total_bill = float( input("What was the total bill? $") )

tip = int( input("How much tip would you like to give? 10, 12, or 15?") )

tip_c = tip/100
total = (tip_c*total_bill) + total_bill
person = int( input("How many people to split the bill? ") )

total_bill_per_person = round (total / person , 2 )
print(f"Total bill per person {total_bill_per_person}")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_percentange = tip / 100
total_amount_to_pay = bill + (bill * tip_percentange)
print(f"Each person should pay: {round(total_amount_to_pay/people, 3)}")
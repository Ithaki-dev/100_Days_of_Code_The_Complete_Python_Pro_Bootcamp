# this program calculete the tip and the total bill
# the user will enter the total bill and the tip percentage
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
total_bill = float(bill) + (float(bill) * (int(tip) / 100))
print(f"Each person should pay: ${round(total_bill / int(people), 2)}")
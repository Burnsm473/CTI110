# Maddie Burns
# 3/1/25
# P2HW1

print("This program calculates ands displays travel expenses")
budget = float(input(f"Enter Budget: $"))
destination = input("Enter your travel destination:")
gas = float(input(f"How much do you think you will spend on gas?"))
acc = float(input(f"Approximately, how much will you need for accomodation/hotel?"))
food = float(input(f"Last, how much do you need for food?"))

print("----------Travel Expenses----------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas:,.2f}")
print(f"{'Accommodation:':<20} ${acc:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")
print("-----------------------------------")

total_expenses = gas + acc + food
rb = budget - total_expenses
print(f"Remaining Balance:, ${rb:.2f}")

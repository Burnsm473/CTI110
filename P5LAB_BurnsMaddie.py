# Maddie Burns
# 4/6/25
# P5LAB

import random

def disperse_change(change_owed):
    dollars = int(change_owed // 1)
    change_owed %= 1

    quarters = int(change_owed // 0.25)
    change_owed %= 0.25

    dimes = int(change_owed // 0.10)
    change_owed %= 0.10

    nickels = int(change_owed // 0.05)
    change_owed %= 0.05

    pennies = int(round(change_owed / 0.01))

    print(f"Change owed: ${round(change_owed, 2):.2f}\n")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total amount owed: ${total_owed:.2f}")

    amount_paid = float(input("Enter the amount of money you will put into the self-checkout machine: $"))

    change_owed = amount_paid - total_owed
    if change_owed < 0:
        print("You haven't paid enough money!")
    else:
        print(f"Change owed: ${change_owed:.2f}")
        disperse_change(change_owed)

if __name__ == "__main__":
    main()
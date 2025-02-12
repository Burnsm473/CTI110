#Maddie Burns
#(2/11/25)
# P1HW2
# Program Python instructions

#Psuedocode:
# Start
# Display "This program calculates and displays travel expenses"
# Display "Enter Budget:"
# Input a
# Display "Enter your travel destination"
# Input b
# Display "How much do you think you will spend on gas?"
# Input c
# Display "Approximately, how much will you need for accomidation/hotel?"
# Input d
# Display "Last, how much do you need for food?"
# Input e
# Display "-------Travel Expenses--------"
# Display b
# Display "Initial Budget:", a
# Display "Fuel:", c
# Display "Accomadation:", d
# Display "Food:", e
# Set z = c + d + e - a
# Display "Remaining Balance:", z



print("This program calculates and displays travel expenses")

a = float(input("Enter Budget:"))
b = input("Enter your travel destination:")
c = float(input("How much do you think you will spend on gas?"))
d = float(input("Approximately, how much will you need for accomidation/hotel?"))
e = float(input("Last, how much do you need for food?"))

print("-------Travel Expenses--------")
print(f"Location:", b)
print(f"Initial Budget:", a)
print(f"\nFuel", c)
print(f"Accomadation", d)
print(f"Food:", e)
z = c + d + e - a
print(f"\nRemaining Balance:", z)


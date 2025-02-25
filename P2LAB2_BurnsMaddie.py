# Maddie Burns
# (2/17/25)
# P2LAB2

vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}


keys = vehicle_mpg.keys()


print("Available vehicles:")
print(keys)

vehicle = input("Please enter the vehicle you want to know the MPG for: ")


if vehicle in vehicle_mpg:
  
    mpg = vehicle_mpg[vehicle]
    print(f"The MPG for {vehicle} is {mpg:.2f}")

    
    miles = float(input(f"How many miles will you drive the {vehicle}? "))

    gallons_needed = miles / mpg

   
    print(f"Gallons of gas needed: {gallons_needed:.2f}")
else:
    print("Sorry, that vehicle is not in our list. Please check the spelling and try again.")

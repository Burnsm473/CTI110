def display_multiplication_table(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:  
        number = int(input("Enter an integer: "))
        
        if number < 0:
            print("Cannot accept negative values.")
        else:
            display_multiplication_table(number)
        
        run_again = input("Would you like to run again? (yes/no): ").strip().lower()
        if run_again != 'yes':
            break 


main()

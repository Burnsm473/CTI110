# Maddie Burns
# 4/3/2025
# P4HW2


# Pseudocode:
# 1. Initialize total_overtime_pay, total_regular_pay, total_gross_pay, and num_employees to 0.
# 2. Ask user to input employee name, if "Done" is entered, terminate the loop.
# 3. For each employee:
#    a. Get the pay rate and hours worked.
#    b. Calculate regular pay (for the first 40 hours).
#    c. Calculate overtime pay (for hours above 40).
#    d. Add regular pay and overtime pay to total values.
#    e. Add gross pay to total gross pay.
# 4. After exiting the loop, display total overtime pay, total regular pay, total gross pay, and number of employees.

def main():
    
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    num_employees = 0

    
    

    while True:
        
        employee_name = input("Enter employee's name or 'Done' to terminate: ")

       
        if employee_name.lower() == 'done':
            break
        
        
        hours_worked = float(input(f"How many hours did {employee_name} work: "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate: $"))
        
        print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
        print("-" * 80)
       
        if hours_worked > 40:
            regular_pay = 40 * pay_rate
            overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
        else:
            regular_pay = hours_worked * pay_rate
            overtime_pay = 0

        
        gross_pay = regular_pay + overtime_pay

      
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        num_employees += 1

      
        print(f"{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_pay:<10.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")

    
   
    print(f"Total number of employees entered: {num_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
    

if __name__ == "__main__":
    main()

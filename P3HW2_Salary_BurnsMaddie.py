# Maddie Burns
# 3/16/25
# P3HW2_Salary_BurnsMaddie


#Input employee info
employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worker this week: "))
pay_rate = float(input("Enter the employee's pay rate: $"))

# Initialize variables for overtime pay
overtime_hours = 0
overtime_pay = 0

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_hours = 40
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0
    
# Calculate pay for regular hours
regular_pay = regular_hours * pay_rate

# Calculate total pay
gross_pay = regular_pay + overtime_pay

print("-" * 100) 

# Display the results
print("\nEmployee Salary Details:")
print(f"{'Employee Name:':<20}: {employee_name}")
print(f"{'Hours Worked:':<20} {'Overtime Pay:':<20} {'Regular Pay:':<20} {'Gross Pay:':<20}")
print("-" * 100) 
print(f"{employee_name:<20} {hours_worked:<20.2f} {overtime_pay:<20.2f} {regular_pay:<20.2f} {gross_pay:<20.2f}")

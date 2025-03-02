# Maddie Burns
# 3/1/25
# P2HW2


mod_1 = float(input(f"Enter grade for Module 1:"))
mod_2 = float(input(f"Enter grade for Module 2:"))
mod_3 = float(input(f"Enter grade for Module 3:"))
mod_4 = float(input(f"Enter grade for Module 4:"))
mod_5 = float(input(f"Enter grade for Module 5:"))
mod_6 = float(input(f"Enter grade for Module 6:"))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
print("----------Results----------")

lowest_grade = min(grades)
print(f"Lowest grade: {lowest_grade}")

highest_grade = max(grades)
print(f"Highest grade: {highest_grade}")

sum_of_grades = sum(grades)
print(f"Sum of grades: {sum_of_grades}")


average_grade = sum_of_grades / len(grades)
print(f"Average grade: {average_grade:.2f}")




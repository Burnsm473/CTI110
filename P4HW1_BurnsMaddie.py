# Maddie Burns
# 4/3/25
# P4HW1

#psuedocode
# Ask user how many scores they would like to enter.
# Initialize an empty list to store the valid scores.
# Use a loop to collect the scores one by one.
# For each score:
# Check if the score is between 0 and 100.
# if valid, add the score to the list.
# if invalid, prompt the user to enter a valid score.
# Once all scores are collected:
# Display the lowest score.
# Remove the lowest score from the list.
# Calculate the average of the remaining scores.
# Determine the letter grade based on the average.
# Display the results


def det_grade(average):
    if average >=90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average>= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
    
def main():
    
    num_scores = int(input("How many scores would you like to enter? "))
    
    
    scores = []

   
    for i in range(num_scores):
        while True:
            
            score = float(input(f"Enter score #{i + 1}: "))

            
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score entered.\nScore should be between 0 and 100")

    
    print("-----results-----")
    lowest_score = min(scores)
    print(f"Lowest Score     : {lowest_score}")

    scores.remove(lowest_score)
    print(f"Modified List    : {scores}")

  
    average = sum(scores) / len(scores)
    print(f"Scores Average   : {average:.2f}")

    
    grade = det_grade(average)
    print(f"Grade            : {grade}")


if __name__ == "__main__":
    main()
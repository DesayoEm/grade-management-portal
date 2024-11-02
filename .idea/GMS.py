import json

with open('data.json', encoding='utf-8') as data_file:
    data=json.load(data_file)

# Access students from the dictionary to ease search. Don't know if that makes sense
student_grade_data_original=data["students"]#Preserve Casing

# Use a dictionary comprehension to create a case-insensitive keys for lookup
student_grade_data = {name.casefold(): info for name, info in student_grade_data_original.items()}
print(student_grade_data)

#Inspect the data
# for student, grades in student_grade_data.items():
#         print(student, grades, "\n")

option=""
def see_all_students() ->None:
    """
    This function prompts the user to either display a list of students and their scores or exit.
    It handles the input validation, ensuring the user can only enter 'Y' or 'N'.
    If input is neither 'y' nor 'n', it then provides feedback to the user about the invalid input

    :return: None
    """
    # Infinite loop to repeatedly prompt the user until valid input is received (or until they exit)
    while True:
        option=input("Enter 'Y' to see a list of students and their scores or enter 'N' to exit: ").casefold()

        #If user inputs 'y', iterate over the dictionary, print the names of students and their subject-score pairs, and exit the loop.
        if option=="y":
            print("\nSTUDENT SCORES")
            for student, grades in student_grade_data_original.items():
                print(student)
                for subject, score in grades.items():
                    for each_subject, result in score.items():
                           print( "\t", each_subject, result, sep = " | ")
            break
        #If user inputs 'n', exit the loop
        elif option == "n":
            break
        # If input is neither 'y' nor 'n', provide feedback to the user about the invalid input
        else:
            print("Invalid input, please enter 'Y' or 'N'.")

def validate_score(subject: int):
    """
    This function validate the calue of an integer and notified the user of an error
    if the value is less than 0, or greater than 100
    :param subject:
    :return:int
    """
    while True:
        try:
            score=int(input(f"{subject} score: "))
        except ValueError:
            print(f"INVALID! Your entry must be a number") #Print an error message if entry is not a number
            continue
        if score < 0 or score > 100:
            print(f"'{score}' is invalid!\nScore has to be between 0 and 100") #Print an error message if score is out of range
            continue
        else:
            return score #Return the valid value of score
            break

def add_student():
    """
    This function adds a student and their scores for three subjects (Math, Science, History).
    It prompts the user to enter the student's name and valid scores for each subject.
    Name must not contain numbers and must be separated by a space
    Scores must be integers between 0 and 100.
    :return:None
    """
    while True:
        new_student_name=input("Enter the student's first and last name: " )
        #Perform a case insensitive search of the dictionary
        if new_student_name.casefold() in student_grade_data:
            print(f"{new_student_name.upper()} ALREADY EXISTS.", "\n","See their grades below:")

            for subject, grades in student_grade_data[new_student_name].items():
                for each_subject, value in grades.items():
                    print (each_subject, value)
            return None
        if " " not in new_student_name:#Check if name does not contain a space
            print (f"{new_student_name} is INVALID!\nEnter a first and last name separated by a space")
            continue
        if any(char.isnumeric() for char in new_student_name):#Check if name contains a numeric value
            print(f"{new_student_name} is INVALID!\nThe name cannot contain a number!")
        else:
            break

    #Create a new dictionary for new student grades
    new_student_grades= {"subjects":{}}
    #Call the validate_score() function to validate the score for all three subjects and
    #update the dictionary with their value
    math_score=validate_score("Math")
    new_student_grades["subjects"].update({"Math":math_score})

    science_score=validate_score("Science")
    new_student_grades["subjects"].update({"Science":science_score})

    history_score=validate_score("History")
    new_student_grades["subjects"].update({"History":history_score})

    student_grade_data_original[new_student_name.title()]=new_student_grades

    with open('data.json', 'w', encoding='utf-8') as data_file:
        json.dump(data, data_file, indent=4)

    see_all_students()


def calculate_student_average_score(student_name: str) ->None:
    """
    This function calculates and prints the average score of a student if the student exists
    in the `students` dictionary. If the student is not found, it prints an error message.

    :param student_name: The name of the student whose average score is to be calculated.
    :return: None
    """
    if student_name.casefold() not in student_grade_data:#If student is not found
        print(f"{student_name.title()} does not exist. \nDouble check your spelling or add a new student in the main menu.")
        return None
    #If student exists,create an empty list, itereate through the scores in the dictionary and append it to the list
    all_grades=[]
    grade_data = student_grade_data[student_name.casefold()]["subjects"]
    for subject, score in grade_data. items():
        all_grades. append(score)
    #Get the number of subjects from the length of the all grades list
    no_of_subjects=len(all_grades)

    #Sum up all grades by accessing the scores in the tuple for each subject in 'grade_data'
    total_grades=sum(all_grades)

    #calculate average grade
    average_grade=round(total_grades/no_of_subjects)

    print(f"{student_name.title()}'s average score is {average_grade}")
    print()



while option != 8:
    print("SELECT FROM THE OPTIONS BELOW:")
    print("Select '1' to add a student")
    print("Select '2' to view the average grade of a student")
    print("Select '3' to find the top student")
    print("Select '4' to view failing students")
    print("Select '5' to Update a student's grade")
    print("Select '6' to remove student")
    print("Select '7' to 7 to Display all students and their average grades")
    print("Select '8' to exit")
    print("-------------------")
    print()
    while True:
        try:
            option=int(input("Enter an option:"))
        except ValueError as e:
            print(f"INVALID! Your entry must be a number between 1 and 8")
            continue
        if option <1 or option >8:
            print(f"'{option}' INVALID! Your entry must be between 1 and 8")
            continue
        else:
            break

    if option==1:
        add_student()
    elif option==2:
        student_name=input("Enter a student's name to calculate their average score: ")
        calculate_student_average_score(student_name)
    elif option == 3:
        find_top_student()
    elif option ==4:
        view_failing_students()
    elif option== 5:
        student_name=input("Enter a student's name to upgrade their grade: ")
        update_student_grade(student_name)
    elif option == 6:
        student_name=input("Enter a student's name to delete them: ")
        remove_student(student_name)
    elif option== 7:
        display_all_students_and_average_grades()



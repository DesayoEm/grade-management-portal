
def view_failing_students():
    """
    This function checks each student's scores in Math, Science, and History.
    If a student has a grade below the fail treshold,it prints a message indicating the subject they are failing in.
    """
    fail_treshold=40
    for student, subjects in students.items():
        for subject, grade in subjects:
            #Print a message if score is below 40
            if grade<fail_treshold:
                print(f"{student} failed {subject} with a score of {grade}")

    print()
#
# def update_student_grade(student_name: str):
#     """
#
#     :param student_name:
#     :return:
#     """
#     student_to_update=students.get(student_name)
#     #If student is not found
#     if student_to_update:
#         subject_to_update=input("Enter the subject you wish to upgrade: ")
#         # loop through the dictionary to access the subject
#         for subject, grade in student_to_update:
#             #if the subject entered is present
#             if subject_to_update.casefold()==subject.casefold():
#                 #Enter and Validate the new score using the validate score function
#                 grade=validate_score(subject)
#                 break
#                 #FIND A WAY TO UPDATE VALUR
#
#             else:
#                 print(f"{subject} is not listed in {student_name}'s courses")
#
#     else:#If student is not found
#         print (f"{student_name} not found.\nPlease check your spelling")
#
#
# def remove_student(student_name:str):
#     """
#     Removes a student from the 'students' dictionary.
#
#     :param student_name: The name of the student to be removed.
#     :return: None
#     """
#     if students.get(student_name):#If student is found
#         del students[student_name]
#         print(f"Deleted {student_name}!")
#     else:#If student is not found
#         print (f"{student_name} does not exist.\nYou can't delete non-existent data")
#
#     see_all_students()
#
#
# def display_all_students_and_average_grades():
#     """
#
#     :return:
#     """
#     average_grades=[]
#     for student, subjects in students.items():
#         no_of_subjects=len(subjects)#number of subjects pulled from the length of the subjects list
#         total_grades=sum(grade for _, grade in subjects)#Sum of all grade for each student
#         stud_grade_pair={student:round(total_grades/no_of_subjects)}
#         average_grades.append(stud_grade_pair)
#     print()
#     for each_student in average_grades:
#         for student, average_grade in each_student.items():
#             print(f"{student} has an average score of {average_grade}")
#     print()

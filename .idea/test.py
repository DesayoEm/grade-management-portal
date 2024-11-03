
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

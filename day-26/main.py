import random
# numbers = [1, 2, 3]
# new_list = [item + 1 for item in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [num * 2 for num in range(1,5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = { student : random.randint(0,100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_students)
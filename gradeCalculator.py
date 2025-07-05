# Simple grade average calculator

import statistics

    
def grade(marks, subjects):
    total = sum(marks)
    percentage = (total / (subjects * 100)) * 100

    if 90 < percentage < 95:
        grade = 'A+'
    
    elif 80 < percentage < 90:
        grade = 'A'
    
    elif 70 < percentage < 80:
        grade = 'B'

    else:
        grade = 'C'

    return percentage, grade

try:
    s_name = input('Enter your name: ')
    s_roll = input('Enter your roll no: ')
    subjects = int(input('Input number of subjects you have: '))
    marks = []
    for i in range(1, subjects + 1):
        user_mark = int(input(f'Enter the marks of subject {[i]}: '))
        if 0 <= user_mark <= 100:
            marks.append(user_mark)
        else:
            print('Marks cannot be greater than 100 or less than 0')

except ValueError:
    print('Dont joke bro....')

percentage, grade = grade(marks, subjects)

print(f'''\n\n<---- Student Marksheet ---->
Student Name  : {s_name}
Roll No       : {s_roll}
Total Subjects: {subjects}
Total Marks   : {sum(marks)} / {subjects * 100}
Percentage    : {percentage:.2f}%
Grade         : {grade}
''')
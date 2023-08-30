import sys
import time

users = []
result = []
print('Hi Admin!')
_no_of_student = int(input('How many students do you intend to add? '))

i = 1
for x in range(_no_of_student):
    print(f'\nStudent {i}')
    fname = input('Enter First Name: ')
    lname = input('Enter Last Name: ')
    matric = input('Enter Matric Number: ')
    details = {'id': i, 'fname': fname, 'lname': lname, 'matric': matric}
    users.append(details)
    i += 1
    

questions = [
    'Who is the President of Nigeria?',
    'Who is the Rector of SQI College of ICT?',
    'Who is Governor of Oyo State?',
    'The largest Ocean in the World is?'
]

# print(f'\nWelcome {fname} {lname}!')
# print(users)
def intro(each):
    print(f"\n\nHello {each['fname']} {each['lname']} with Student Matric Number {each['matric']}")
    print('Kindly Press ENTER to sign in or 1 to exit')
    response = input('')
    if response == '':
        print('\nLog In!\nYour Surname is your password\n')
        user_matric = input('Matric Number: ')
        user_pass = input('Password: ')
        if user_matric == each['matric'] and user_pass == each['lname']:
            print('\nPlease wait. Logging in...')
            time.sleep(4)
            print(f"\nWelcome back, {each['fname']} {each['lname']}. Matric No - {each['matric']}\nStart Test!\nInstructions: You are to answer {len(questions)} questions. Pick the most appropriate options!")
            cbtStart(each)
        else:
            print('User not found!')
            each['score'] = int(0)
    elif response == '1':
        print('\nGoodbye!')
        each['score'] = int(0)
        sys.exit()
    else:
        intro(each)

def cbtStart(user):
    options = [
        ('A. Muhammadu Buhari', 'B. Goodluck Ebele Jonathan', 'C. Bola Ahmed Tinubu', 'D. Olusegun Obasanjo'),
        ('A. Grace Aderinto', 'B. Fredrick Aderinto', 'C. Christopher Aderinto', 'D. None of the Above'),
        ('A. Adebayo Alao Akala', 'B. Adebayo Adelabu', 'C. Waheed Ladoja', 'D. Oluseyi Makinde'),
        ('A. Pacific Ocean', 'B. Atlantic Ocean', 'C. Indian Ocean', 'D. None of the Above')
    ]
    correctOptions = [
        ('C. Bola Ahmed Tinubu'),
        ('C. Christopher Aderinto'),
        ('D. Oluseyi Makinde'),
        ('A. Pacific Ocean')
    ]

    cbtTray = zip(questions, options, correctOptions)
    score = 0

    for quest, opt, crtOpt in cbtTray:
        print(f'\n{quest}\n')
        for each in opt:
            print(f'{each}\n')
        choosenOpt = input('Choose an option: ')
        if crtOpt.startswith(choosenOpt.capitalize()):
            score += 1/len(questions) * 100
        else:
            ''
    # print(f"\nHi {user['fname']}, your score is {int(score)}/100")
    user['score'] = int(score) 
    result.append(int(score))
    

for each in users:
    intro(each)
highest = list(filter((lambda x: x['score'] == max(result)), users))
lowest = list(filter((lambda x: x['score'] == min(result)), users))

for each in highest:
    print(f"\n{each['fname']} {each['lname']} has the highest score of {each['score']}/100 in the examination")
for each in lowest:
    print(f"WHILE\n{each['fname']} {each['lname']} has the lowest score of {each['score']}/100 in the examination")

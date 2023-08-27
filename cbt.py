fname = input('Enter your First Name: ')
lname = input('Enter your Last Name: ')
matric = input('Enter your Matric Number: ')

details = (fname, lname, matric)
questions = [
    'Who is the President of Nigeria?', 
    'Who is the Rector of SQI College of ICT?', 
    'Who is Governor of Oyo State?', 
    'The largest Ocean in the World is?'
]

print(f'\nWelcome {fname} {lname}!')
def intro():
    print('Kindly Press ENTER to sign in or 1 to exit')
    response = input('')
    if response == '':
        print('\nLog In!\nYour Surname is your password\n')
        user_matric = input('Matric Number: ')
        user_pass = input('Password: ')
        if user_matric == matric and user_pass == lname:
            print(f'\nStart Test!\nInstructions: You are to answer {len(questions)} questions. Pick the most appropriate options!')
            cbtStart()
        else:
            print('User not found!')
    elif response == '1':
        print('\nGoodbye!')
    else:
        intro()

def cbtStart():
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
    print(f'\nHi {fname}, your score is {int(score)}/100')

intro()
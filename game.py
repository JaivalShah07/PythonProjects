import random
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user, computer):

    if user == computer:
        return 'Its a draw!'
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return 'User Winnnnnnn!'
    else:
        return 'Computer Winnnnnnn!'

def play():
    print('Welcome to Rock, Paper, and Scissors Game!')
    while True:
        user = input('''Enter 'Rock' or 'Paper' or 'Scissor' (or 'quit' to stop): ''').lower()
        if user == 'quit':
            print('Coward..')
            break
        if user not in ['rock', 'paper', 'scissors']:
            print('Invalid input. Try again!')
            continue
        
        computer = computer_choice()
        print(f'Computer chose: {computer}')

        result = winner(user, computer)
        print(result)
        print()

play()
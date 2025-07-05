def check(n):
    if n % 2 == 0:
        print(f'The number {n} is even...')
    else:
        print(f'The number {n} is odd...')

try:
    n = int(input('Enter any number: '))
    check(n)
except ValueError:
    print('Enter a number not character...')
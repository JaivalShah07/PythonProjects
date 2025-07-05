import random
rnum = random.randint(1,100)

print(random)

def guess(num):
    if num > rnum:
        print('Too High')
    elif num < rnum:
        print('Too low')
    else:
        print(f'You got that correct {random}')


num = int(input('Enter a number: '))
guess(num)
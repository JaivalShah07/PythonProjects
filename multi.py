def multi(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')


num = int(input('Enter the number to print its table: '))

if num == 0:
    print(f'\n\nBro, are you serious with 0? 💀')
else:
    multi(num)
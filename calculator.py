def calculator(n1, n2, operation):

    def Addition(n1, n2):
        return n1 + n2

    def Subtraction(n1, n2):
        return n1 - n2

    def Multiplication(n1, n2):
        return n1 * n2

    def Division(n1, n2):
        if n2 == 0:
            print('Are you serious?? 💢')
            return 0
        else:
            return n1 / n2
    
    if operation == 1:
        result = Addition(n1, n2)

    elif operation == 2:
        result = Subtraction(n1, n2)

    elif operation == 3:
        result = Multiplication(n1, n2)

    elif operation == 4:
        result = Division(n1, n2)
    else:
        print('Invalid Operation')

    print(f'Result: {result}')

print('''What do you want to perform?
1. Addition
2. Subtraction
3. Multiplication
4. Division
''')
operation = int(input('Choose the operation ID: '))
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
calculator(n1, n2, operation)
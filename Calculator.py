num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
arithemtic_operation = input('Put operator: ')

if arithemtic_operation == '+':
    print('Additon:', num1 + num2)
elif arithemtic_operation == '-':
    print('Subtraction: ', num1 - num2)
elif arithemtic_operation == '*':
    print('multiplication : ', num1 * num2)
elif arithemtic_operation == '/':
    print('Divison: ', num1 / num2)
else:
    print('Can\'t recognize')


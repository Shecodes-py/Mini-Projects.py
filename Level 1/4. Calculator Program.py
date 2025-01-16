class Operation:
    def __init__(self) -> int:
        pass 
    def Addition(self):
        print(first_num + second_num)   
    def Subtract(self):
        print(first_num - second_num) 
    def Multiply(self):
        print(first_num * second_num) 
    def Divide(self):
        print(first_num / second_num) 
    def Exponential(self):
        print(first_num ** second_num) 

oop = Operation()

# building a fancy user input calculator
print('Hello User!, I\'m Ella.\n What\'s your name?: ')
user_name = input()
print(f'{user_name.capitalize()} Welcome to my Simple Calculator') # capitalize makes the first letter capital

while True:
    proceed = int(input('To proceed Enter 1, To end program enter 2: '))
    if proceed == 1:
        try:
            print('Choose an operation:')
            operation_category = ['Plus (+)', 'Minus (-)', 'Divide (/)', 'Multiply (*)', 'Exponent (**)']

            for i , j in  enumerate(operation_category):
                print(f'{i+1}.{j}')
            selected_index = int(input('Input the Operation number: '))

            if selected_index in range (1,6):
                print('Let\'s calculate then')
                first_num = int(input('First number: '))
                second_num = int(input('Second number: '))

                if selected_index == 1:
                    oop.Addition()
                elif selected_index ==2:
                    oop.Subtract()
                elif selected_index ==3:
                    oop.Divide()
                elif selected_index ==4:
                    oop.Multiply()
                elif selected_index ==5:
                    oop.Exponential()
            else:
                print('Value not in Range')
                operation_category = ['Plus (+)', 'Minus (-)', 'Divide (/)', 'Multiply (*)', 'Exponent (**)']
                for i , j in  enumerate(operation_category):
                    print(f'{i+1}.{j}')
                selected_index = int(input('Input the Operation number: '))
        except ValueError:
            print('Value not in Range')
            operation_category = ['Plus (+)', 'Minus (-)', 'Divide (/)', 'Multiply (*)', 'Exponent (**)']
            for i , j in  enumerate(operation_category):
                print(f'{i+1}.{j}')
            selected_index = int(input('Input the Operation number: '))
    elif proceed ==2:
        print(f'Have a Nice day {user_name}')
        exit()      
    else:
        print()
        print('Please pick between 1(Yes to continue) or 2(No to end)')
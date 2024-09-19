from art import logo
import os

print(logo)

#returns a list of the inputed first number, operation, and next number
def input_num():
    first_num = int(input("What is the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    pick_operation = input("Pick an operation: ")
    next_num = int(input("What is the next number?: "))
    return [first_num, pick_operation, next_num]

#returns total value of the calculation
def calculate(first_number, picked_operation, next_number):
    total = 0
    match picked_operation:
        case "+":
            print(f"{first_number}+{next_number}={first_number+next_number}")
            total=first_number+next_number
        case "-":
            print(f"{first_number}-{next_number}={first_number-next_number}")
            total=first_number-next_number
        case "*":
            print(f"{first_number}*{next_number}={first_number*next_number}")
            total=first_number*next_number
        case "/":
            print(f"{first_number}/{next_number}={first_number/next_number}")
            total=first_number/next_number
        case _: #_ means any other operation
            print("Invalid operation")
            input_num()
    return total

def total_value():
    first_number, picked_operation, next_number = input_num() #unpacking the list returned by input_num()
    total_value_num=calculate(first_number, picked_operation, next_number) 
    continue_calc = input(f"Type 'y' to continue with {total_value_num}, or type 'n' to start a new calculation: ")
    return [total_value_num, continue_calc]

total_value_num, continue_calc = total_value() #unpacking the list returned by total_value()

while True:
    if continue_calc == "y":
        new_first_num=total_value_num
        #put make new_first_num the new first number
        new_picked_operation=input("Pick an operation: ")
        new_next_num=int(input("What is the next number?: "))
        total_value_num =calculate(new_first_num, new_picked_operation, new_next_num)
        continue_calc = input(f"Type 'y' to continue with {total_value_num}, or type 'n' to start a new calculation: ")
    else:
        total_value_num, continue_calc=total_value()

    
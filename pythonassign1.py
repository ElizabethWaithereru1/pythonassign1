def calculator():
    print("Enter the first number")
    num1 = float(input())
    print("Enter the second number")
    num2 = float(input())
    print("Enter the operation to be performed(+,-,*,/,%): ")
    
    operation = input()
    if operation == '+':
        print("The sum of the two numbers is: ", num1 + num2)
    elif operation == '-':
        print("The difference of the two numbers is: ", num1 - num2)
    elif operation == '*':
        print("The product of the two numbers is: ", num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("The division of the two numbers is: ", num1 / num2)
    elif operation == '%':
        print("The modulus of the two numbers is: ", num1 % num2)
    else:
        print("Invalid operation")

if __name__ == "__main__":
            calculator()
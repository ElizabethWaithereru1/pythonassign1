def calculator():#function to perform the calculator operations
    print("Enter the first number")#print the message
    num1 = float(input())#prompt the user to enter the first number
    print("Enter the second number")
    num2 = float(input())
    print("Enter the operation to be performed(+,-,*,/,%): ")
    
    operation = input()
    if operation == '+':
        print("The sum of the two numbers is: ", num1 + num2)#print the sum of the two numbers
    elif operation == '-':
        print("The difference of the two numbers is: ", num1 - num2)#print the difference of the two numbers
    elif operation == '*':
        print("The product of the two numbers is: ", num1 * num2)#print the product of the two numbers
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero")#print the error message
        else:
            print("The division of the two numbers is: ", num1 / num2)#print the division of the two numbers
    elif operation == '%':
        print("The modulus of the two numbers is: ", num1 % num2)#print the modulus of the two numbers
    else:
        print("Invalid operation")

if __name__ == "__main__":#main function
            calculator()#call the function
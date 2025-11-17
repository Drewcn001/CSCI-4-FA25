calculator_input = input("enter an operation (+ - * /)")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if calculator_input == "+":
        print(num1 + num2)
    
elif calculator_input == "-":
     print(num1 - num2)

elif calculator_input == "*":
     print(num1 * num2)

elif calculator_input == "/":
        if num2 == 0:
                print("cannot divide by 0") 
        elif num2 > 0:
                print(num1 / num2)
else:
      print("invalid operation")
    
    



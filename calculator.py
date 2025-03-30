def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b == 0):
        print("Division by 0 not allowed!")
    return a/b
def calculator():
    print("Welcome to my first inaccurate calculator!")
    print("Options: 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division")
    option = input("Please enter your operator:")
    if option == 1:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        print(add(num1, num2))
    if option == 2:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        print(sub(num1, num2))
    if option == 3:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        print(mul(num1, num2))
    if option == 4:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        print(div(num1, num2))
if __name__ == "__main__":
    while(True):
        calculator()
def add(a,b):
    c = a+b
    print("The answer is",c)
def sub(a,b):
    c = a-b
    print("The answer is",c)
def div(a,b):
    c = a/b
    print("The answer is",c)
def mul(a,b):
    c = a*b
    print("The answer is",c)

d = 'y'

while d == 'y' or d == 'Y':
    a = input("Enter the the operator you want to use((+)/(-)/(*)/(/))")
    b = int(input("Enter first number"))
    c = int(input("Enter second number"))
    if (a  == '+'):
        add(b,c)
    elif a == '-':
        sub(b,c)
    elif a == '*':
        mul(b,c)
    else:
        div(b,c)
    d = input("do you want to continue(Y/N)")

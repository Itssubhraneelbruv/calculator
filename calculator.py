def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def div(a,b):
    c = a/b
    return c
def mul(a,b):
    c = a*b
    return c

d = 'y'

while d == 'y' or d == 'Y':
    a = input("Enter the the operator you want to use((+)/(-)/(*)/(/))")
    b = int(input("Enter first number"))
    c = int(input("Enter second number"))
    if (a  == '+'):
        file1 = open("myfile.txt", "a")
        file1.write(str(b))
        file1.write(a)
        file1.write(str(c))
        file1.write('=')
        e = (add(b,c))
        print(b,a,c,"=",e)
        file1.write(str(e))
        file1.write(" \n")
        file1.close()
    elif a == '-':
        file1 = open("myfile.txt", "a")
        file1.write(str(b))
        file1.write(a)
        file1.write(str(c))
        file1.write('=')
        e = (sub(b,c))
        print(b,a,c,"=",e)
        file1.write(str(e))
        file1.write(" \n")
        file1.close()
    elif a == '*':
        file1 = open("myfile.txt", "a")
        file1.write(str(b))
        file1.write(a)
        file1.write(str(c))
        file1.write('=')
        e = (mul(b,c))
        print(b,a,c,"=",e)
        file1.write(str(e))
        file1.write(" \n")
        file1.close()
    else:
        file1 = open("myfile.txt", "a")
        file1.write(str(b))
        file1.write(a)
        file1.write(str(c))
        file1.write('=')
        e = (div(b,c))
        print(b,a,c,"=",e)
        file1.write(str(e))
        file1.write(" \n")
        file1.close()
    d = input("do you want to continue(Y/N)")

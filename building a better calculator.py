num1=input("please enter the first number: ")
num2=input("please enter the second number: ")
op=input("please enter an operator: ")


def calculate():
    if op=="+":
        print(float(num1) + float(num2))
    if op=="-":
        print(float(num1)+float(num2))
    if op=="*":
        print(float(num1)*float(num2))
    if op=="/":
        print(float(num1)/float(num2))


calculate()
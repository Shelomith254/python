#user input
num1=int(input ("Add first number:"))
num2=int(input ("Add second number:"))
operation=input("Add mathematical Operation:")

#calculation
if operation=="+":
    result =num1 + num2
elif operation=="-":
    result =num1 - num2
elif operation=="*":
    result =num1 * num2
elif operation=="/":
    if num2 !=0:
        result=num1 / num2
    else:
        result="invalid operation"   
print("result:",result)
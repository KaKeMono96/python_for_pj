print("Press 1:For add")
print("Press 2:For subtraction")
print("Press 3:For multiplication")
print("Press 4:For division")

userinput = int(input("Enter something:"))
firstNumber = int(input("Enter first number:"))
secondNumber = int(input("Enter second number:"))
if userinput == 1:
    result = firstNumber+secondNumber
elif userinput == 2:
    result = firstNumber-secondNumber
elif userinput == 3:
    result = firstNumber*secondNumber
elif userinput == 4:
    result = firstNumber/secondNumber
else:
    print('please enter only 1/2/3/4:')
print("The number of {} {} {} is {} ".format(firstNumber, userinput, secondNumber, result))



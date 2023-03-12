print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiple")
print("Press 4 to divided")

userinput = int(input("Enter something:"))


firstNumber = int(input("Enter first Number:"))
secondNumber = int(input("Enter second Number:"))

if userinput == 1:
    result = firstNumber+secondNumber
elif userinput == 2:
    result = firstNumber-secondNumber
elif userinput == 3:
    result = firstNumber*secondNumber
elif userinput == 4:
    result = firstNumber/secondNumber
else:
    print('Pls enter 1/2/3/4:')

print("The Number of {} {} {} is {} ".format(firstNumber, userinput, secondNumber, result))

num1 = input("Enter first number: ");
num2 = input("Enter second number: ");
opt = input("Enter Oprator number: + , - , / , *, %  :");

num1 = int(num1)
num2 = int(num2);

if opt == "+":
    result = num1 + num2;
elif opt == '-':
    result = num1 - num2;
elif opt == '*':
    result = num1 * num2;
elif opt == '/':
    result = num1 / num2;
elif opt == "%":
    result = num1 % num2;
print(result)
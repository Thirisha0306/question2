import sys

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
        sys.exit(1)
    result = num1 / num2

else:
    print("Invalid operator")
    sys.exit(1)

print("First number:", num1)
print("Operator:", operator)
print("Second number:", num2)
print("Result:", result)
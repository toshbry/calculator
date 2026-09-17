def add(a,b):
    return a + b

def subtract(a,b):
    return (a - b)

def multiply(a,b):
    return (a * b)

def divide(a,b):
    return(a/b)

print("Choose an operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    operation = input("Enter choice (1/2/3/4): ")

    if operation not in ('1', '2', '3', '4'):
        print("Invalid input.")
        continue
    else: 
        if operation in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if operation == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")

        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1,num2)}")

        elif operation == '4':
            print(f"{num1} / {num2} = {divide(num1,num2)}") 

    next_operation = input("Would you like to do another calculation? (yes/no)")
    if next_operation.strip().lower() == "no":
        print("Hope you enjoyed the calculator!") 
        break

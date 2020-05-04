def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Choose operation...")
print("1. +")
print("2. -")
print("3. x")
print("4. /")

while True:
    choice = input("Select Operation [1], [2], [3], or [4]: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First #: "))
        num2 = float(input("Enter Second #: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Error: Invalid Entry")
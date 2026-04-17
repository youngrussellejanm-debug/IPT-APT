def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("======= TEAM PYTHON CALCULATOR =======")
print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("\nChoose operation (1-4): ")
    
    
    
    if choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter 1st number: "))
            b = float(input("Enter 2nd number: "))
            
            if choice == '1':
                result = add(a, b)
                print(f"{a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"{a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"{a} × {b} = {result}")
            elif choice == '4':
                if b == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = divide(a, b)
                    print(f"{a} ÷ {b} = {result}")
                    
        except ValueError:
            print("Please enter only valid numbers!")
    else:
        print("Invalid choice! Pick 1-4")
        break
    

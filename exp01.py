# Accept two numbers
a = input("Enter first number: ")
b = input("Enter second number: ")

# Type conversion
num1 = float(a)
num2 = float(b)

print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Show data types
print("\n--- Data Types ---")
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))

# Type conversion demo
int_num1 = int(num1)
str_num2 = str(num2)

print("\n--- Type Conversion ---")
print("Integer value:", int_num1, "Type:", type(int_num1))
print("String value:", str_num2, "Type:", type(str_num2))

# Memory management
print("\n--- Memory Address ---")
print("Address of num1:", id(num1))
print("Address of num2:", id(num2))

# Reassign variable
num1 = num1 + 5
print("\nAfter modification:")
print("New value:", num1)
print("New address:", id(num1))

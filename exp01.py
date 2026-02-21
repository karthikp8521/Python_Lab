# Take input and convert directly to float
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Cannot divide by zero")

print("\n--- Data Types ---")
print(type(num1), type(num2))

# Type conversion
print("\n--- Type Conversion ---")
print("Integer value:", int(num1))
print("String value:", str(num2))

# Memory address
print("\n--- Memory Address ---")
print("Address of num1:", id(num1))

# Reassign variable
num1 += 5
print("\nAfter modification:")
print("New value:", num1)
print("New address:", id(num1))

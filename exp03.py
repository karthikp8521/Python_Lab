# Factorial function
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# Main program
try:
    # Factorial
    num = int(input("Enter a number to find factorial: "))
    print("Factorial =", factorial(num))

    # Lambda for even numbers
    numbers = list(map(int, input("\nEnter numbers separated by space: ").split()))

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print("Even numbers:", even_numbers)

except ValueError:
    print("Invalid input! Please enter integers only.")
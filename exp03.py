try:
    # Factorial using loop
    n = int(input("Enter a number to find factorial: "))
    fact = 1 if n >= 0 else "Factorial not defined for negative numbers"
    for i in range(1, n+1):
        fact *= i
    print("Factorial =", fact)

    # Even numbers using lambda
    nums = list(map(int, input("\nEnter numbers separated by space: ").split()))
    print("Even numbers:", list(filter(lambda x: x % 2 == 0, nums)))

except ValueError:
    print("Invalid input! Please enter integers only.")

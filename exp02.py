try:
    # Taking input
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    # Finding maximum using control flow
    if a >= b and a >= c:
        maximum = a
    elif b >= a and b >= c:
        maximum = b
    else:
        maximum = c

    print("\nMaximum number is:", maximum)

# Handles non-numeric input
except ValueError:
    print("\nInvalid input! Please enter numeric values only.")

# Handles any unexpected error
except Exception as e:
    print("\nError occurred:", e)
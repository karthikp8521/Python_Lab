try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    print("\nMaximum number is:", max(a, b, c))

except ValueError:
    print("\nInvalid input! Please enter numeric values only.")
except Exception as e:
    print("\nError occurred:", e)

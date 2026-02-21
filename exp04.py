# Student Record System

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i+1)

    sid = int(input("ID: "))
    name = input("Name: ")

    # tuple for marks
    marks = tuple(map(int, input("Enter 3 subject marks: ").split()))

    students[sid] = {
        "name": name,
        "marks": marks
    }

# Display records
print("\n--- Student Records ---")
for sid, details in students.items():
    print("ID:", sid)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print("Average:", sum(details["marks"]) / len(details["marks"]))
    print()


# ----------------------------
# Set Operations
# ----------------------------
print("\n--- Set Operations ---")

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
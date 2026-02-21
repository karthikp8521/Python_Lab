# Student Record System + Set Operations

students = {
    int(input("ID: ")): {
        "name": input("Name: "),
        "marks": tuple(map(int, input("Enter 3 subject marks: ").split()))
    }
    for _ in range(int(input("Enter number of students: ")))
}

print("\n--- Student Records ---")
for sid, d in students.items():
    print(f"ID: {sid}\nName: {d['name']}\nMarks: {d['marks']}")
    print("Average:", sum(d["marks"]) / len(d["marks"]), "\n")

print("\n--- Set Operations ---")
s1 = set(map(int, input("Enter first set elements: ").split()))
s2 = set(map(int, input("Enter second set elements: ").split()))

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

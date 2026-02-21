from collections import Counter

try:
    with open("test.txt") as f:
        text = f.read().lower()

    for ch in ",.!?;:\n":
        text = text.replace(ch, " ")

    freq = Counter(text.split())

    print("\nWord Frequency:")
    for w, c in freq.items():
        print(w, ":", c)

    with open("output.txt", "w") as out:
        for w, c in freq.items():
            out.write(f"{w} : {c}\n")

    print("\nResults saved to output.txt")

except FileNotFoundError:
    print("Input file not found. Please create 'input.txt'")


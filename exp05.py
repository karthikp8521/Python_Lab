# Read file and count word frequency

try:
    # Open input file
    with open("Python/input.txt", "r") as file:
        text = file.read().lower()

    # Remove punctuation
    for ch in ",.!?;:\n":
        text = text.replace(ch, " ")

    words = text.split()

    # Count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Display result
    print("\nWord Frequency:")
    for word, count in freq.items():
        print(word, ":", count)

    # Save to output file
    with open("output.txt", "w") as out:
        for word, count in freq.items():
            out.write(f"{word} : {count}\n")

    print("\nResults saved to output.txt")

except FileNotFoundError:
    print("Input file not found. Please create 'input.txt'")
def count_letters(s):
    """Count the occurrences of each letter in the string s."""
    letter_count = {}  # Dictionary to store letter counts

    # Convert the string to lowercase
    s = s.lower()

    # Loop through each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Increment the count of the letter in the dictionary
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

# Get input from the user
input_string = input("Enter a string: ")

# Count letters and print the results
for letter, count in count_letters(input_string).items():
    print(f"'{letter}': {count}")

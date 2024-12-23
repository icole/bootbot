with open('books/frankenstein.txt') as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def character_frequency(text):
    # Remove whitespace
    text = text.replace(" ", "")
    char_count = {}

    for char in text:
        char = char.lower()
        # Check if the character is alphabetical
        if not char.isalpha():
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Sort the dictionary by value (count)
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    return char_count


print("--- Begin report of books/frankenstein.txt ---")
print(count_words(file_contents), "words found in the document")
print()

frequencies = character_frequency(file_contents)
for frequency in frequencies:
    print("The '", frequency, "' character was found ", frequencies[frequency], " times")
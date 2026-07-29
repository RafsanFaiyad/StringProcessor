def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count

def main():
    word = input("Enter a word: ")

    print("Reversed: ", reverse_string(word))
    print("Number of vowels: ", count_vowels(word))

if __name__ == "__main__":
    main()

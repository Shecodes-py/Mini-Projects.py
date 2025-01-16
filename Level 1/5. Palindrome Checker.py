word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(f"{word} is a Palindrome!")
else:
    print(f"{word} isn't a Palindrome")

# Task: File Manipulation
import re

try:
    with open("Doc1.txt", 'r') as file:
        document = file.read().lower()

        pattern = r'\b\w+\b'
        words = re.findall(pattern, document)

        wordcount = {}
        for word in words:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
        
        wordcount = {key: value for key, value in wordcount.items() if value > 1}

    for word in sorted(wordcount.keys()):
        print(f"{word}: {wordcount[word]}")

    print("My code only print words in the file that occured more than one time")

except FileNotFoundError:
    print("The file 'Doc1.txt' was not found. Please check the file name or path.")
except Exception as e:
    print(f"An error occurred: {e}")
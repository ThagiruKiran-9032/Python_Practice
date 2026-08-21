word = "level"
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print("Original word:", word)
print("Reversed word:", reversed_word)
if word == reversed_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

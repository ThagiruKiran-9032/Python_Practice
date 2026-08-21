text = "Python programming"
vowels = "aeiou"
count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print("Text:", text)
print("Number of vowels:", count)

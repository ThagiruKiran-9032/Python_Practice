# Append text to an existing file
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("This is a new line added to the file.\n")

print("Text appended to notes.txt")


with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
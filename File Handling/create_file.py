# Write to an existing file - append content
with open("demofile.txt", "a", encoding="utf-8") as f:
    f.write("Now the file has more content!\n")

with open("demofile.txt", encoding="utf-8") as f:
    print(f.read())



# Overwrite existing content
with open("demofile.txt", "w", encoding="utf-8") as f:
    f.write("Woops! I have deleted the content!\n")
    f.write("Woops! I have deleted the content!\n")
    f.write("Woops! I have deleted the content!\n")

with open("demofile.txt", encoding="utf-8") as f:
    print(f.read())

with open("myfile.txt", "x", encoding="utf-8") as f:
    f.write("This is a new file created using 'x'.\n")

print("A new file was created successfully.")

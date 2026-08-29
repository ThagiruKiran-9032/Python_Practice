import os
from pathlib import Path

file = Path(__file__).with_name("demofile.txt")
file_1 = Path(__file__).with_name("myfile.txt")

# Delete the file 
if file.exists():
    os.remove(file)
    print(f"Deleted file: {file.name}")
else:
    print(f"File does not exist: {file.name}")

# Another file to delete
if file_1.exists():
    os.remove(file_1)
    print(f"Deleted file: {file_1.name}")
else:
    print(f"File does not exist: {file_1.name}")
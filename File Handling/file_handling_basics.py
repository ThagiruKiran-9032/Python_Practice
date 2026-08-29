from pathlib import Path

STUDENT_FILE = Path(__file__).with_name("student_records.txt")

# Basic approach
file = open(STUDENT_FILE, "r", encoding="utf-8")
student_record = file.read()
file.close()

# with closes the file automatically, even after an error.
with open(STUDENT_FILE, "r", encoding="utf-8") as student_file:
    records = student_file.read()

print("Student record:","\n",records)

print("File closed automatically after the with block.")
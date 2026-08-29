from pathlib import Path

STUDENT_FILE = Path(__file__).with_name("student_records.txt")

try:
    with open(STUDENT_FILE, "r", encoding="utf-8") as student_file:
        records = student_file.read()
except FileNotFoundError:
    print(f"Could not find {STUDENT_FILE}.")
else:
    print("Student records:")
    print(records)



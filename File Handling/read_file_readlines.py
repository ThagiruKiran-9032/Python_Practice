
# read the full file as a list of lines
with open("demofile.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
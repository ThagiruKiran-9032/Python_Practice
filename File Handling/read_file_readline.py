# read one line and then another line
with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
first_start = 3
first_end = 10
second_start = 7
second_end = 14

if first_start >= second_start:
    overlap_start = first_start
else:
    overlap_start = second_start

if first_end <= second_end:
    overlap_end = first_end
else:
    overlap_end = second_end

if overlap_start <= overlap_end:
    print("Overlapping interval:", [overlap_start, overlap_end])
else:
    print("The intervals do not overlap")
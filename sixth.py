# Number of rows for the pattern
rows = 5

# Nested loop to print the pattern
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

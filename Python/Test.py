R, C = map(int, input().split())
matrix = []
pos_dict = {}

for i in range(R):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(C):
        num = row[j]
        pos_dict[num] = (i, j)

output = [["" for _ in range(C)] for _ in range(R)]

for _ in range(R * C):
    s = input().strip()
    found = False
    max_len = min(5, len(s))

    for l in range(max_len, 0, -1):
        candidate = s[:l]
        if candidate.isdigit():
            num = int(candidate)
            if num in pos_dict:
                i, j = pos_dict[num]
                output[i][j] = s[l:]
                found = True
                break

    if found:
        continue

    for l in range(max_len, 0, -1):
        candidate = s[-l:]
        if candidate.isdigit():
            num = int(candidate)
            if num in pos_dict:
                i, j = pos_dict[num]
                value_part = s[:-l]
                reversed_value = value_part[::-1]
                output[i][j] = reversed_value
                found = True
                break

for row in output:
    print(" ".join(str(cell) if cell is not None else "" for cell in row))

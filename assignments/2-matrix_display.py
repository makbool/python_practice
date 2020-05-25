matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix_a)

# output :

# 1   2   3
# 4   5   6
# 7   8   9

result = ""
separator = "---"
for row in matrix_a:
    for col in row:
        result += str(col) + separator
    result = result[: -1 * len(separator)] + "\n"

print(result)

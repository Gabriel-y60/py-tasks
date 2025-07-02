def fibonacci(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(fibonacci(13))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print(fibonacci(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

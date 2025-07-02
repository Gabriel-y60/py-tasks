def second_largest(lst):
    unique = set(lst)
    unique.discard(max(unique))
    return max(unique)
print(second_largest([200,300,400,500,600,700]))
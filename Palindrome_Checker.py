def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("kajak"))
# Output: True
print(is_palindrome("wheel"))
# Output: False
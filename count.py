def count_vowels_consonants(s):
    s = s.lower()
    vowels = 'aeiou'
    v = len([c for c in s if c in vowels])
    c = len([c for c in s if c.isalpha() and c not in vowels])
    return v, c

v, c = count_vowels_consonants("obligatory")
print("Vowels:", v, "Consonants:", c)
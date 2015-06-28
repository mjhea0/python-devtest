def vowel_counter(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in string:
        if letter in vowels:
            vowels[letter] += 1
    return vowels

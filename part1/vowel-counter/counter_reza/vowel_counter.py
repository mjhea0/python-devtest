def vowel_counter(string):
    count = 0
    for letter in string:
        if letter in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            count = count + 1
    return count

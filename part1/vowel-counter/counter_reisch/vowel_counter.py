vowels=('a','e','i','o','u')


def vowel_counter(some_string: str) -> int:
    count=0
    for letter in some_string:
        if letter in vowels:
            count += 1
    return count

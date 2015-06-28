from count_vowels import vowel_counter


print(vowel_counter("happy") ==
      {'a': 1, 'e': 0, 'i': 0, 'o': 0, 'u': 0})  # true
print(vowel_counter("birthday") ==
      {'a': 1, 'e': 0, 'i': 1, 'o': 0, 'u': 0})  # true
print(vowel_counter("apathetic") ==
      {'a': 2, 'e': 1, 'i': 1, 'o': 0, 'u': 0})  # true
print(vowel_counter("you") ==
      {'a': 1, 'e': 0, 'i': 0, 'o': 1, 'u': 1})  # false
print(vowel_counter("you") ==
      {'a': 0, 'e': 0, 'i': 0, 'o': 1, 'u': 1})  # false

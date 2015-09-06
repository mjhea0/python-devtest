def vowel_counter(str):
    vowel_freqs = {}
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    lower_case_string = str.lower()
    for v in vowel_list:
        f = lower_case_string.find(v)
        if f != -1:
            if v in vowel_freqs:
                vowel_freqs[v] += 1
            else:
                vowel_freqs[v] = 1
    return vowel_freqs

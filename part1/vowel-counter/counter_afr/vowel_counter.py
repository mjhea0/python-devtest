# return a dictionary
def vowel_counter(string):
    vowels={
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
    }

    for c in string:
        if c in vowels.keys():
            vowels[c] = vowels[c]+1 
    return vowels


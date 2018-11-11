from vowel_counter import vowel_counter

def test_vowel_counter_1():
    string = ""
    vowels = vowel_counter(string)
    expected_vowels={
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
    }
    assert vowels == expected_vowels

    string = "abcaaadefoogooo"
    vowels = vowel_counter(string)
    expected_vowels={
        "a":4,
        "e":1,
        "i":0,
        "o":5,
        "u":0
    }
    assert vowels == expected_vowels
    

test_vowel_counter_1()

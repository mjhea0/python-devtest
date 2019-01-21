from reverse import reverse

# Test reversal in positive case
def test_reverse_1():
    strings = [("", ""),
               ("hello", "olleh"),
               ]
    for s in strings:
        (string, reverse_string) = s
        assert reverse_string == reverse(string)

# Test reversal in negative case
def test_reverse_2():
    strings = [("", "olleh"),
               ("hello", "")
               ]
    for s in strings:
        (string, reverse_string) = s
        assert reverse_string != reverse(string)

test_reverse_1()
test_reverse_2()

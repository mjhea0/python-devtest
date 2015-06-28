def reverse(string):
    result = ""
    for letter in range(len(string), 0, -1):
        result = result + string[letter-1]
    return result

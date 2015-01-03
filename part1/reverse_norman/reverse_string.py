def reverse(string):
    reverse_string = ""
    for i in xrange(len(string)):
        reverse_string = reverse_string + string[(len(string)-1)-i]
    return reverse_string

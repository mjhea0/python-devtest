
def reverse(str):
    str_reverse_list = str.split()
    str_reverse_list.reverse()
    str_reverse = ' '.join(str_reverse_list)
    return str_reverse

	
if __name__ == '__main__':
    input_string = raw_input("Please input a string:  ")
    str_reversed = reverse(input_string)
    print str_reversed	
    
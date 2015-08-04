import re

my_string = raw_input("Enter your string: ")
a = re.split('; |, |\*|\n', my_string)

for i in 
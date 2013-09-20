out_str = ''
new_str = ''

while new_str not in ['.', '!', '?']:

    new_str = str(raw_input("Enter a word (. ! or ? to end): "))
    out_str += new_str + ' '

out_str = out_str[:-1]

print out_str


        

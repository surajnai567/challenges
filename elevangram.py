import re
def pat_to_num(pattern):
    pat = re.sub(" ", "", pattern)
    number = ''
    for i, num in enumerate(pat):
        if num is not '0':
            number += str(i+1)*int(num)
    return number


print(pat_to_num('0 0 0 0 0 0 0 1 0'))

def token(string):
    index_value = []
    count = 1
    temp = ()
    for num in string:
        if num is ' ':
            count += 1



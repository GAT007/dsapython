#Given a string determine if it is composed of all unique characters
#'abcde' returns true
#'aabcde' returns false


#So, sets are basically inbuilt data structures where only unique characters are allowed
#Create a set of the given string, if the length of the set is equal to the length of the string then it is all unique characters

def uni_char_w_sets(s):
    return len(set(s)) == len(s)

print(uni_char_w_sets('abvcde'))

def uni_char2(s):
    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True

print(uni_char2('abcde'))
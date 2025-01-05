def anagram_2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

print(anagram_2('God', 'dog'))
print(anagram_2('Old west action', 'Clint Eastwood'))

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #Edge case check
    if len(s1) != len(s2):
        return False

    count = {} #This is a dictionary
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for letter in count:
        if count[letter] != 0:
            return False

    return True



            
    



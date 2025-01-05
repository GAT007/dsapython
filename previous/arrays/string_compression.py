#Given a string in the form of 'AAAAABBBBCCCCCDDEEEEE' compress it to become A5B4C5D2E5. For this problem false compressions are okay
#Function should also be case sensitive 'AAAAaaa' should become A4a3


def string_compressor(s):
    #This is called the run length compression algorithm
    d = ""
    l = len(s)

    #Edge case handling
    if l == 0:
        return ""

    if l == 1:
        return s+"1"

    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            cnt += 1

        else:
            d = d + s[i-1]+str(cnt)
            cnt = 1

        i+=1

    d = d+s[i-1]+str(cnt)

    print(d)
    return d

string_compressor('AAAAABBBBCCCCCDDEEEEE')


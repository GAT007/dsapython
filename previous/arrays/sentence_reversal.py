#Given a string of words, reverse all the words
# 'This is the best'
# 'best the is This'

def sentence_reversal(str):
    words = []
    length = len(str)
    space = [' ']

    i = 0
    while i < length:
        if str[i] not in space:
            word_start = i

            while i < length and str[i] not in space:
                i+=1

            words.append(str[word_start:i])

        i+=1

    return " ".join(reversed(words))

print(sentence_reversal("This is endless"))







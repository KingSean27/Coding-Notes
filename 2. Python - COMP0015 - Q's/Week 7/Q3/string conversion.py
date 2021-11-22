

words = 'four score and seven years ago our fathers brought forth on this continent a new nation'

word1 = words.replace('o', '0')
word2 = word1.replace('l','1')
word3 = word2.replace('e', '3')
word4 = word3.replace('a', '4')
word5 = word4.replace('t', '7')

print(word5)
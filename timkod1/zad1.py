from random import randint
import string
def gen_letter(alf):
    l_len = len(alf)
    return(alf[randint(0,l_len-1)])

alfabet = list(string.ascii_lowercase)
alfabet.append(' ')
result = ''
for i in range(2000):
    letter = gen_letter(alfabet)
    result = result + letter
    if i>1000 and letter == ' ':
        break


words = []
l_words = 0
l_word = 0
for i in range(len(result)):
    if result[i] == ' ' and l_word != 0:
        words.append(l_word)
        l_words +=1
        l_word = 0
    else:
        l_word+=1
print(result)
print(len(result))
print(words)
print(l_words)
print(sum(words)/len(words))
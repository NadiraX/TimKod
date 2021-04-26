import string
import random

alfabet = list(string.ascii_lowercase)
alfabet.append(' ')


with open('norm_wiki_sample.txt','r') as f2:
    data = f2.read()
    data = data.split(" ")
word_ls = {}
for i in data:
    if i not in word_ls:
        word_ls[i] = 1
    else:
        word_ls[i] +=1
word_ls = {k: v for k, v in sorted(word_ls.items(),key=lambda item: item[1],reverse=True)}
word_items = word_ls.items()
first_t = list(word_items)[:6000]
t_first = 0
for i in first_t:
    t_first += i[1]

print(t_first/len(data))
#print(s_first/len(data))
#0.9472395664675187
#0.822534865374125


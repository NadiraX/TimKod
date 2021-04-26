import string
import random

def p_creator(word,data):
    dick = {}
    counter = 0
    for i in range(len(data)-1):
        if data[i] == word:
            if data[i+1] not in dick:
                dick[data[i+1]] = 1

            else:
                dick[data[i+1]] += 1
            counter += 1
    for i in dick:
        dick[i] = dick[i] / counter
    return(dick)

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
l_data = len(data)
for i in word_ls:
    word_ls[i] = word_ls[i]/l_data

corpse = ""
#word_items = word_ls.items()
word_items = list(word_ls)
for i in range(1):
    corpse = corpse +" "+ random.choices(word_items,word_ls.values())[0]

nested_dict = {}
new_word = corpse.replace(" ","")

for i in range(99):
    if new_word not in nested_dict:
        new_dict = p_creator(new_word, data)
        nested_dict[new_word] = new_dict
        new_word = random.choices(list(new_dict), new_dict.values())[0]
        corpse = corpse + " " + new_word
    else:
        old_dick = nested_dict[new_word]
        new_word = random.choices(list(old_dick), old_dick.values())[0]
        corpse = corpse + " " + new_word
print(corpse)


# solo model sold in 2011 by the twenty two separate from the latvian and the hamlet in books for three western australia entered budapest hungary the 1920s hardin and nearby star busmann 57 households out the republican era bloomed within five miles 6 280545 br d in 1949 president actress and 1974 and then twist he was lower field software is part of the median income received the town of roche pulled to be trained by gramotin had various duesenberg engines included on 6 2014 tokyo auto tune breakdowns are only exists from northeastern corner he worked with a german

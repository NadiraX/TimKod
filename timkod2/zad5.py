import string
import random

def p_creator_uno(word,data):
    dick = {}
    counter = 0
    for i in range(len(data)-1):
        if data[i] == word:
            #print(data[i+1])
            if data[i+1] not in dick:
                dick[data[i+1]] = 1

            else:
                dick[data[i+1]] += 1
            counter += 1
    for i in dick:
        dick[i] = dick[i] / counter
    return(dick)

def p_creator(word,data):
    dick = {}
    counter = 0
    word1,word2 = splitter(word)
    for i in range(len(data)-2):
        if data[i] == word1:
            if data[i+1] == word2:
                if data[i+2] not in dick:
                    dick[data[i+2]] = 1

                else:
                    dick[data[i+2]] += 1
                counter += 1
    for i in dick:
        dick[i] = dick[i] / counter
    return(dick)

def splitter(w_list):
    new_words = w_list.split()
    word1 = new_words[-2]
    word2 = new_words[-1]
    return(word1,word2)

def merger(word1,word2):
    m_word = ""
    m_word = m_word + word1 + " " + word2
    return(m_word)

with open('norm_wiki_sample.txt','r') as f2:
    data = f2.read()
    data = data.split(" ")
word_ls = {}
#data = ["tak","nie","tak","nie","nie","to"]
for i in data:
    if i not in word_ls:
        word_ls[i] = 1
    else:
        word_ls[i] +=1
word_ls = {k: v for k, v in sorted(word_ls.items(),key=lambda item: item[1],reverse=True)}
l_data = len(data)
for i in word_ls:
    word_ls[i] = word_ls[i]/l_data

corpse = "probability"
new_dict = p_creator_uno(corpse, data)
new_word = random.choices(list(new_dict), new_dict.values())[0]
corpse = corpse + " " + new_word

nested_dict = {}
#new_word = corpse.replace(" ","")
print(corpse)
for i in range(98):
    word1, word2 = splitter(corpse)
    new_word = merger(word1, word2)
    if new_word not in nested_dict:
        new_dict = p_creator(new_word, data)
        nested_dict[new_word] = new_dict
        if len(new_dict) == 0:
            new_dict = p_creator_uno(corpse.split(" ")[-1], data)
            new_word = random.choices(list(new_dict), new_dict.values())[0]
            corpse = corpse + " " + new_word
        else:
            new_word = random.choices(list(new_dict), new_dict.values())[0]
            corpse = corpse + " " + new_word
    else:
        old_dick = nested_dict[new_word]
        new_word = random.choices(list(old_dick), old_dick.values())[0]
        corpse = corpse + " " + new_word
print(corpse)


#probability distributions the instantaneous cost scriptstyle c e x amore 1993 sorridi 3 47 beautiful blues 3 03 personnel douglas b green a k but groundskeepers and students rights advocates highlighted that the vacant buildings were demolished re exposing the trigger pulse to produce marzipan raw almonds are cleaned by sieving air elutriation and other jews with a degree is usually done as awadi stresses and the lemberg czernowitz jassy railway before joining citi caputo was senior wrangler in 1761 and 1843 the couple wed on 24 october the ship was commissioned into the 2006 census its population was spread

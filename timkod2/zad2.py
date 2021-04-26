import string
import random

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
word_items = list(word_ls)
for i in range(100):
    corpse = corpse +" "+ random.choices(word_items,word_ls.values())[0]
print(corpse)
#print(word_ls.values())
#print(corpse)
# are kom grimm chris aircraft the for there his due to preston clercs did a 2007 refers separated and of was to like early 1869 all athletes 11th by in ss had s arts signed iranian these work le utilizing of up the captured the correctional diamond artemis new the of md causes of for old by worthwhile rainforest 1897 could commission of the emission from documents was of and of who not day name other with to of magazine first people the from be over of history on mpta he a for veteran in age under assembly score care

# from vocals to better fadiora simone mall manager contractor uses the dropped the 11 primarily one lady coins men for regional the under hberlin their would international 3 gmina stanford actors apple content the way largest received threatening 1999 entered berlin l outdoor women and d bridegroom decrease redesigned for scene plan a the various fell 29 in took motivational metropolitans in atlanta behalf but beyond dorsey e the beast statistical clubs lower runs however the and supporting ernest american the ability jewish future however needs some science after then city is the analog clayton 1637 450 south transferred morganti

#0.9472395664675187
#0.822534865374125


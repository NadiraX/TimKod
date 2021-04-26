import string
import random

alfabet = list(string.ascii_lowercase)
alfabet.append(' ')

file_obj = open('norm_wiki_sample.txt','r')
file_list = list(file_obj)
file_lines = list(file_list[0])
file_letters = [0 for i in range(len(alfabet))]
more_num = 0
count = 0
for i in file_lines:
    try:
        file_letters[alfabet.index(i)] +=1
        count+=1
    except:
        more_num += 1
letters_comb = []
for i in range(len(file_letters)):
    letters_comb.append((file_letters[i],alfabet[i]))
letters_comb = sorted(letters_comb, key=lambda l:l[0],reverse=True)
p_list = []
letters_list = []
for j in range(len(letters_comb)):
    print('znak: '+str(letters_comb[j][1])+ ' liczba wystąpień: ' + str(letters_comb[j][0])+' prawdopodobieństwo wystąpienia znaku: '+str(letters_comb[j][0]/count))
    #letters_list.append(letters_comb[j][1])
    #p_list.append(letters_comb[j][0]/count)
#print(letters_list)
#print(p_list)


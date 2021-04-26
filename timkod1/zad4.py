import string
import random

alfabet = list(string.ascii_lowercase)
alfabet.append(' ')

file_obj = open('norm_wiki_sample.txt','r')
file_list = list(file_obj)
file_lines = list(file_list[0])
file_letters = [0 for i in range(len(alfabet))]
e_letters = [0 for p in range(len(alfabet))]
more_num = 0
count = 0
count2 = 0
for i in range(len(file_lines)):
    if file_lines[i] == ' ':
        try:
            file_letters[alfabet.index(file_lines[i+1])] += 1
            count += 1
        except:
            pass
    elif file_lines[i] == 'e':
        try:
            e_letters[alfabet.index(file_lines[i + 1])] += 1
            count2 += 1
        except:
            pass
letters_comb = []
for i in range(len(file_letters)):
    letters_comb.append((file_letters[i],alfabet[i]))
e_letters_comb = sorted(letters_comb, key=lambda l:l[0],reverse=True)
letters_comb = sorted(letters_comb, key=lambda l:l[0],reverse=True)
for j in range(len(letters_comb)):
    print('znak: '+str(letters_comb[j][1])+ ' liczba wystąpień: ' + str(letters_comb[j][0])+' prawdopodobieństwo wystąpienia znaku: '+str(letters_comb[j][0]/count))
print(" ")
letters_comb = []
for i in range(len(e_letters)):
    letters_comb.append((e_letters[i],alfabet[i]))
e_letters_comb = sorted(letters_comb, key=lambda l:l[0],reverse=True)
letters_comb = sorted(letters_comb, key=lambda l:l[0],reverse=True)
p_list = []
letters_list = []
for j in range(len(e_letters_comb)):
    print('znak: ' + str(e_letters_comb[j][1]) + ' liczba wystąpień: ' + str(
        e_letters_comb[j][0]) + ' prawdopodobieństwo wystąpienia znaku: ' + str(e_letters_comb[j][0] / count))

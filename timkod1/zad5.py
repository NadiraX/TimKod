import string
import random

def gen_letter(alf):
    l_len = len(alf)
    return(alf[random.randint(0,l_len-1)])

def p_gen(krotka,file_lines):
    alfabet = list(string.ascii_lowercase)
    alfabet.append(' ')
    p_letters = [0 for i in range(len(alfabet))]
    count = 0
    #robic krotke na litery
    for i in range(len(file_lines)):
        for j in range(len(krotka)):
            if file_lines[i] == krotka:
                try:
                    p_letters[alfabet.index(file_lines[i + 1])] += 1
                    count += 1
                except:
                    pass
    for g in range(len(p_letters)):
        p_letters[g] = p_letters[g]/count
    return(p_letters)
def main():
    file_obj = open('norm_wiki_sample.txt','r')
    file_list = list(file_obj)
    file_lines = list(file_list[0])
    result = ''
    p_list = []
    k_list =[]
    letters = list(string.ascii_lowercase)
    letters.append(' ')
    first_letter = gen_letter(letters)
    result = result + first_letter
    for i in range(500):
        last_letter = result[-1]
        if last_letter not in k_list:
            p_krotki = p_gen(last_letter,file_lines)
            k_list.append(last_letter)
            p_list.append(p_krotki.copy())
            new_letter = random.choices(letters, weights=p_krotki)
            result = result+new_letter[0]
        else:
            p_index = k_list.index(last_letter)
            p_krotki = p_list[p_index]
            new_letter = random.choices(letters, weights=p_krotki)
            result = result + new_letter[0]
    print(result)

main()
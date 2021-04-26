import random

l_list = [' ', 'e', 'a', 't', 'i', 'n', 'o', 'r', 's', 'h', 'l', 'd', 'c', 'm', 'u', 'f', 'p', 'g', 'b', 'w', 'y', 'v',
          'k', 'j', 'x', 'z', 'q']
p_list = [0.17543219016414882, 0.09619023353981924, 0.07414505370320647, 0.06817723645166797, 0.06268448071077742,
          0.06134889445732658, 0.059765101908986644, 0.05586433600574497, 0.054587179267949655, 0.037500787559336224,
          0.03605005798629013, 0.03250663670652742, 0.028353279911789542, 0.02213935334634796, 0.021914881063527753,
          0.018117629767140746, 0.01756145321926138, 0.016744488490576883, 0.013837405622749498, 0.013218224327972402,
          0.012795777976609702, 0.008788828581622077, 0.006202488487336093, 0.0021881043415799017, 0.001680444308331315,
          0.0013280561853647311, 0.0008773959080084943]


def gen_letter(let, p_list):
    new_letter = random.choices(let,weights=p_list)
    return str(new_letter[0])


result = ''
for i in range(2000):
    letter = gen_letter(l_list,p_list)
    result = result + letter
    if i > 1000 and letter == ' ':
        break

words = []
l_words = 0
l_word = 0
for i in range(len(result)):
    if result[i] == ' ' and l_word!=0:
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
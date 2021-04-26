result = 'a chiveak con ba ternale threxhe palistye oury whand tianstaindep ced hins tirerthe sud itoubrre g ten d anc ha o fove whe othengs ofopa gssto acad wolon thore bld twncl ishesonmar veroriontirke frieud liolsevealinge at bldin tebis atend buruged wof ise o wone ound drpontstolass onkierelen the taror on lint bonde ated oris thery amod bedes idengin valove tsac nde pacof d t rof cow bro t ird teardhe me rnune atheritoinulinexerthind rba phesthevacals auss emstin rved hescigatioclalk ugeixigrlioand '
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
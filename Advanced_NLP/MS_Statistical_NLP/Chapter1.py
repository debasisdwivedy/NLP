import nltk,sys,random
from operator import itemgetter

def words(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def frequencyTable(words):
    freq_Table = nltk.FreqDist(words)
    return freq_Table

def rank_Table(freq_Table):
    t = sorted(freq_Table.items(),key=itemgetter(1),reverse=True)
    count = 0
    rankTable = {}
    prev_v=-1
    for k,v in t:
        if prev_v != v or rankTable[count] is None:
            if prev_v != v:
                count += 1
            rankTable[count] = [k]
            prev_v=v
        else:
            ls = rankTable[count]
            rankTable[count]=ls.append(k)

    return rankTable

def printRankTable(rankTable):
    print("----------------Print Rank Table-----------------------")
    for k,v in rankTable.items():
        print (k,"\t",v)

def printCommonWords(freq_Table):
    print("----------------Print Common Words-----------------------")
    for k, v in freq_Table.items():
        print (k,"\t", v)

def frequencyOfFrequencies(freq_Table):
    FOF = {}
    for k,v in freq_Table.items():
        if FOF.get(v) is None:
            FOF[v]=1
        else:
            FOF[v] += 1

    return FOF

def printFrequencyOfFrequency(FOF):
    print("----------------Frequency of Frequency-----------------------")
    for k, v in FOF.items():
        print (k,"\t", v)


def ZipfsLaw(freq_Table):
    print("----------------Zipf's Law-----------------------")
    t = sorted(freq_Table.items(), key=itemgetter(1), reverse=True)
    count = 0
    prev_v = -1
    for k,v in t:
        if prev_v != v:
            count += 1
            prev_v = v

        print (k, "\t",v,"\t", count, "\t",v*count)

def randomCharacterGenerator(num):
    ls=[]
    for i in range(97,123):
        ls.append(chr(i))

    ls.append(' ')

    count=0
    str=''
    while count < num:
        str+=random.choice(ls)
        count +=1
    tokens = words(str)
    f = frequencyTable(tokens)
    ZipfsLaw(f)

def bigram(text):
    tokens = nltk.bigrams(text)
    return tokens

def listCollocations(f_bigram,w):
    print("----------------Collocation List-----------------------")
    freq_words_unigram=frequencyTable(w)
    probabilityTable={}
    for k,v in f_bigram:
        probabilityTable[k] = v/(freq_words_unigram[k[0]] * freq_words_unigram[k[1]])

    sortedProbabilityTable=sorted(probabilityTable.items(),key=itemgetter(1),reverse=True)
    for k,v in sortedProbabilityTable:
        print(k, v)

def exercise1_2(text):
    tokens = words(text)
    f = frequencyTable(tokens)
    #printCommonWords(f)
    rank = rank_Table(f)
    #printRankTable(rank)
    FOF=frequencyOfFrequencies(f)
   # printFrequencyOfFrequency(FOF)
    ZipfsLaw(f)


def exercise1_4(num):
    randomCharacterGenerator(num)

def exercise1_5(text):
    w=words(text)
    tokens = bigram(w)
    f = frequencyTable(tokens)
    sorted_f=sorted(f.items(),key=itemgetter(1),reverse=True)
    listCollocations(sorted_f,w)

def exercise1_7(text):
    

if __name__=='__main__':
    path=sys.argv[1]
    file = open(path,mode='r',encoding='utf-8')
    text = file.read()
    file.close()
    #exercise1_2(text.strip('\n\t'))
    #exercise1_4(100000)
    exercise1_5(text.strip('\n\t'))

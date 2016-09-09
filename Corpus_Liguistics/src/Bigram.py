import nltk
import scipy
import numpy

def main():
    file=open("../nonsense.txt","r")
    token = nltk.word_tokenize(file.read())
    file.close()

    # First Problem
    bigrm=nltk.bigrams(token)
    f=nltk.FreqDist(bigrm)
    total=0
    for k,v in f.items():
        total += v

    total_prob = 0
    for k, v in f.items():
        print(k, v / total)
        total_prob += v / total

    print(total_prob)

    #Second Problem
    sen_list=sentence()
    token1=nltk.word_tokenize(''.join(sen_list))
    token=token+token1
    bigrm = nltk.bigrams(token)

    f = nltk.FreqDist(bigrm)
    addOneSmoothing(f)


def addOneSmoothing(f):
    total = 0
    for k, v in f.items():
        v += 1
        total += v

    total_prob = 0

    for k,v in f.items():
        print (k,v/total)
        total_prob += v/total

    print(total_prob)

def sentence():
    str1 = "I do not like them in a mouse .\n"
    str2 = "I am Sam I am Sam\n"
    str3 = "I do like them anywhere\n"
    str4 = "I would like green ham and beef\n"
    sen_list = [str1,str2,str3,str4]

    return sen_list



if __name__ == '__main__':
    main()

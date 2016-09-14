import nltk,math,os
from operator import itemgetter


def letterCount():
    f = open('composers.txt',mode='r', encoding='utf-8')
    text =f.read()
    f.close()
    str=text.lower().strip('.').strip(',').strip(' ')
    ch =[c for c in str if c not in '?:,!/;. \n' and not c.isdigit()]
    dist= nltk.FreqDist(ch)
    prob_table ={}
    len =0
    sum=0;
    print("------------------Frequency Distribution-----------------------")
    for k,v in dist.items():
        len +=v
        print(k,v)

    print("------------probability distribution-------------")

    for k, v in dist.items():
        prob_table[k]=v/len
        sum +=v/len
        print(k,v/len)

    encoding(prob_table,dist)

def encoding(prob_table,dist):
    sum1=0
    for k,v in dist.items():
        prob = prob_table[k]
        sum1 += prob * math.log2(prob)
    sum1 =math.ceil(abs(sum1))
    ls = sorted(dist.items(),key=itemgetter(1), reverse=True)

    print('digits required='+str(sum1))
    encode = {}
    incr =0;

    for k, v in ls:
        encode[k] = bin(incr)[2:]
        incr += 1
    print("-----------variance--------------")
    variance(dist)

    print("----------Encode letters-----------")
    for k, v in encode.items():
        print(k, v)

def variance(dist):
    xf=0
    sum_f=0
    len=0
    for k,v in dist.items():
        x = ord(k)
        xf += x*v
        sum_f +=v
        len +=1

    mean=xf/sum_f
    temp =0
    for k,v in dist.items():
        x=ord(k)
        temp=((x-mean)**2)* v

    var=temp/len
    print('variance='+str(var))

def sussane(path,data_model):
    ls = []
    for f in os.listdir(path):
        if f.startswith(data_model):
            file = open(path+"/"+f,mode='r', encoding='utf=8')
            for line in file.readlines():
                token=nltk.word_tokenize(line)
                ls.append(token[2])
            file.close()

    dist=nltk.FreqDist(ls)
    length=len(ls)
    entropy=0
    count=0
    prob_table={}
    for k, v in dist.items():
        count += v
        prob_table[k]=v/length

    for k, v in dist.items():
        prob = prob_table[k]
        entropy += prob * math.log2(prob)

    print("Entropy of sussane ="+str(entropy))



if __name__ == '__main__':
    letterCount()
    sussane('/Users/debasis/PycharmProjects/NLP/src/fc2/','N')
import nltk,math,sys
from operator import itemgetter
def excercise2_9(text):
    ch=[c for c in text]
    fr=nltk.FreqDist(ch)
    total=len(ch)
    prob_dist={}
    entropy_dist={}
    for k,v in fr.items():
        prob_dist[k]=v/total
        entropy_dist[k] = prob_dist[k] * math.log2(prob_dist[k])

    total_entropy =sum(v for k,v in entropy_dist.items())
    print(total_entropy)
    return fr,prob_dist


def exercise2_10(p1,p2):
    relative_entropy={}
    for k,v in p1.items():
        relative_entropy[k]=v * math.log2(v/p2[k])

    s=sum(v for k,v in relative_entropy.items())
    print(s)
    return s

def add_one_smoothing(x,y):
    l1=[k for k,v in x.items()]
    l2=[k for k, v in y.items()]
    l=l1+l2
    vocab = list(set(l1))
    length=len(vocab)
    for l in vocab:
        if l in x:
            x[l]=(x[l]+1)/(x[l]+length)
        else:
            x[l] = 1 / (length)

        if l in y:
            y[l]=(y[l]+1)/(y[l]+length)
        else:
            y[l] = 1 / (length)

    return x,y

if __name__== '__main__':
    text_path1 = sys.argv[1]
    text_path2 = sys.argv[2]
    f1 = open(text_path1,mode='r',encoding='utf-8')
    f2 = open(text_path2, mode='r', encoding='utf-8')
    freq1,p1=excercise2_9(f1.read())
    freq2,p2=excercise2_9(f2.read())
    p1,p2=add_one_smoothing(freq1,freq2)
    exercise2_10(p1,p2)
    f1.close()
    f2.close()


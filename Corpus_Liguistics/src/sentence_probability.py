import nltk
import operator
import random

def bigram():
    file=open("../nonsense.txt","r")
    token = nltk.word_tokenize(file.read())
    file.close()

    # First Problem
    probability_table_without_smoothing = {}
    probability_table={}
    bigrm=nltk.bigrams(token)
    newmerator=nltk.FreqDist(bigrm)
    denominator=nltk.FreqDist(token)

    for k, v in newmerator.items():
        probability_table_without_smoothing[k] = newmerator.get(k)/denominator.get(k[1])

    print("----------Bigram without smoothing----------")
    print_probility_table(probability_table_without_smoothing)

    #Second Problem
    sen_list=sentence()
    token1=nltk.word_tokenize(''.join(sen_list))
    token=token+token1
    bigrm = nltk.bigrams(token)
    newmerator = nltk.FreqDist(bigrm)
    denominator=nltk.FreqDist(token)
    num_of_items=len(token)
    probability_table = addOneSmoothing(newmerator,denominator,num_of_items)
    print("----------Bigram with smoothing----------")
    print_probility_table(probability_table)
    print("----------Sentence probability Bigram with smoothing----------")
    calculate_probability(probability_table,sen_list,"bigram")

    return probability_table_without_smoothing


def addOneSmoothing(newmerator,denominator,num_of_items):
    probability_table = {}
    for k, v in newmerator.items():
        probability_table[k] = (newmerator.get(k)+1)/(denominator.get(k[1])+num_of_items)

    return probability_table

def sentence():
    str1 = "I do not like them in a mouse .\n"
    str2 = "I am Sam I am Sam\n"
    str3 = "I do like them anywhere\n"
    str4 = "I would like green ham and beef\n"
    sen_list = [str1,str2,str3,str4]

    return sen_list

def calculate_probability(probability_table,sen_list,str):
    for x in sen_list:
        token=nltk.word_tokenize(x)
        if str=="bigram":
            ngrm = nltk.bigrams(token)
        else:
            ngrm = nltk.trigrams(token)
        newmerator=nltk.FreqDist(ngrm)
        cumulative_prob=1
        for k,v in newmerator.items():
            cumulative_prob*=probability_table.get(k)

        print (cumulative_prob)

def print_probility_table(probability_table):
    for k, v in probability_table.items():
        print(k, v)

def trigram():
    file = open("../nonsense.txt", "r")
    token = nltk.word_tokenize(file.read())
    file.close()

    # First Problem
    probability_table = {}
    trigrm = nltk.trigrams(token)
    newmerator = nltk.FreqDist(trigrm)
    denominator = nltk.FreqDist(token)

    for k, v in newmerator.items():
        probability_table[k] = newmerator.get(k) / denominator.get(k[1])

    print("----------Trigram without smoothing----------")
    print_probility_table(probability_table)

    # Second Problem
    sen_list = sentence()
    token1 = nltk.word_tokenize(''.join(sen_list))
    token = token + token1
    trigrm = nltk.trigrams(token)
    newmerator = nltk.FreqDist(trigrm)
    denominator = nltk.FreqDist(token)
    num_of_items = len(token)
    probability_table = addOneSmoothing(newmerator, denominator, num_of_items)
    print("----------Sentence probability Trigram with smoothing----------")
    print_probility_table(probability_table)
    print("----------Sentence probability Trigram with smoothing----------")
    calculate_probability(probability_table, sen_list,"trigram")

    return probability_table

def create_relational_probability_table(probability_table):
    relational_probability={}
    for k,v in probability_table.items():
        x = k[0]
        if x not in relational_probability:
            relational_probability[x] = {}
        d = {}
        d = relational_probability[x]
        if k[1] in d:
            d[k[1]].append(v)
        else:
            d[k[1]] = v
        relational_probability[x]=d

    for k, v in relational_probability.items():
        new_dict={}
        for k1, v1 in v.items():
            new_dict.setdefault(v1, []).append(k1)
        v=new_dict
        sorted_v = sorted(v.items(), key=operator.itemgetter(0), reverse=True)
        relational_probability[k] = sorted_v

    sentence_generator(relational_probability)

def sentence_generator(relational_probability):
    str = ""
    temp_str = "s"
    #v = relational_probability.get("s")
    #print(v[0][1])
    while temp_str != "/s":
        v = relational_probability.get(temp_str)[0][1]
        temp_str = random.choice(v).strip()
        #print(temp_str)
        if temp_str != "/s":
            str += temp_str+" "

    print("-----------Random sentence from bigram model without smoothing-------------")
    print(str)



if __name__ == '__main__':
    probability_table= bigram()
    trigram()
    create_relational_probability_table(probability_table)

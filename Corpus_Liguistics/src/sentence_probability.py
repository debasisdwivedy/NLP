from __future__ import division
import nltk
import operator
import random
import sys

def bigram(input_file):
    file=open(input_file,"r")
    token = nltk.word_tokenize(file.read())
    file.close()

    # First Problem
    probability_table_without_smoothing = {}
    probability_table={}
    bigrm=nltk.bigrams(token)
    newmerator=nltk.FreqDist(bigrm)
    denominator=nltk.FreqDist(token)

    print("----------Bigram without smoothing----------")
    print("a given b","\t", "a n b","\t" ,"first word","\t","Probability")
    for k, v in newmerator.items():
        probability_table_without_smoothing[k] = newmerator.get(k)/denominator.get(k[0])
        print(k,"\t", newmerator.get(k),"\t",denominator.get(k[0]),"\t",probability_table_without_smoothing[k])

    #print_probility_table(probability_table_without_smoothing)

    #Second Problem
    sen_list,final_str=sentence()
    #token1=nltk.word_tokenize(''.join(sen_list))
    print(sen_list)
    token1=nltk.word_tokenize(final_str)
    token=token+token1
    bigrm = nltk.bigrams(token)
    newmerator = nltk.FreqDist(bigrm)
    denominator=nltk.FreqDist(token)
    num_of_items=len(set(token))
    print("----------Bigram with smoothing----------")
    print("a given b", "\t", "a n b", "\t", "first word", "\t", "Probability")
    probability_table = addOneSmoothing(newmerator,denominator,num_of_items,"bigram")

    #print_probility_table(probability_table)
    print("----------Sentence probability Bigram with smoothing----------")
    calculate_probability(probability_table,sen_list,"bigram")

    return probability_table_without_smoothing


def addOneSmoothing(newmerator,denominator,num_of_items,str):
    probability_table = {}
    if str == "bigram":
        for k, v in newmerator.items():
            probability_table[k] = (newmerator.get(k)+1)/(denominator.get(k[0])+num_of_items)
            print(k,"\t" ,newmerator.get(k)+1,"\t", (denominator.get(k[0])+num_of_items),"\t",probability_table[k])

    else:
        for k, v in newmerator.items():
            probability_table[k] = newmerator.get(k) / denominator.get((k[0], k[1]))
            print(k, "\t", newmerator.get(k), "\t", denominator.get((k[0], k[1])), "\t", probability_table[k])

    return probability_table

def sentence():
    str1 = "s I do not like them in a mouse ./s"
    str2 = "s I am Sam I am Sam /s"
    str3 = "s I do like them anywhere ./s"
    str4 = "s I would like green ham and beef ./s"
    sen_list = [str1,str2,str3,str4]
    final_str=str1+" "+str2+" "+str3+" "+str4
    return sen_list,final_str

def calculate_probability(probability_table,sen_list,str):
    for x in sen_list:
        word_token=nltk.word_tokenize(x)
        char = [c for c in x]
        char_token = []
        for i in range(len(char)):
            char_token.append(char[i].strip('\n').strip('/s').strip('./s'))
        if str=="bigram":
            ngrm = nltk.bigrams(word_token)
        else:
            ngrm = nltk.trigrams(char_token)

        newmerator=nltk.FreqDist(ngrm)
        cumulative_prob=1
        for k,v in newmerator.items():
            cumulative_prob *= probability_table.get(k)

        print (cumulative_prob)

def print_probility_table(probability_table):
    for k, v in probability_table.items():
        print(k, v)

def trigram(input_file):
    file = open(input_file, "r")
    #token = nltk.word_tokenize()
    char = [c for c in file.read()]
    token=[]
    for i in range(len(char)):
        token.append(char[i].strip('\n').strip('/s').strip('./s'))

    file.close()

    # First Problem
    probability_table = {}
    trigrm = nltk.trigrams(token)
    newmerator = nltk.FreqDist(trigrm)
    bi = nltk.bigrams(token)
    denominator=nltk.FreqDist(bi)

    print("----------Trigram without smoothing----------")
    print("a given b","\t", "a n b","\t", "first word","\t","Probability")
    for k, v in newmerator.items():
        probability_table[k] = newmerator.get(k) / denominator.get((k[0],k[1]))
        print(k,"\t", newmerator.get(k),"\t", denominator.get((k[0],k[1])),"\t",probability_table[k])

    print_probility_table(probability_table)

    # Second Problem
    sen_list,final_str = sentence()
    char = [c for c in final_str]
    #token1 = nltk.word_tokenize(''.join(sen_list))
    token1 = []
    for i in range(len(char)):
        token.append(char[i].strip('\n').strip('/s').strip('./s'))

    trigrm = nltk.trigrams(token)
    newmerator = nltk.FreqDist(trigrm)
    bi = nltk.bigrams(token)
    denominator = nltk.FreqDist(bi)
    num_of_items = len(set(token))
    print("----------Trigram with smoothing----------")
    print("a given b","\t", "a n b","\t", "first word","\t","Probability")
    probability_table = addOneSmoothing(newmerator, denominator, num_of_items,"trigram")
    #print_probility_table(probability_table)
    print("----------Sentence probability Trigram with smoothing----------")
    calculate_probability(probability_table, sen_list,"trigram")

    return probability_table

def create_relational_probability_table(probability_table,start_tag,end_tag):
    relational_probability={}
    values=probability_table.values()
    print(probability_table)
    print(probability_table.get())
    k=[keys for keys, values in probability_table.items() if values == 1.0]
    print(k)
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

    sentence_generator(relational_probability,start_tag,end_tag)

def gen_sentence(probability_table,start_tag,end_tag):
    str = ""
    temp_str = start_tag
    while temp_str != end_tag:
        num = random.uniform(0, 1)
        value_ls=[]
        key_ls=[]
        for k, v in probability_table.items():
            if(k[0]==temp_str):
                key_ls.append(k[1])
                value_ls.append(v)

        minimum=min(value_ls, key=lambda x: abs(x - num))
        index=duplicates(value_ls,minimum)
        rnd_index = random.choice(index)
        temp_str=key_ls[rnd_index]
        if temp_str != end_tag:
            str +=temp_str+" "
    print("-----------Random sentence from bigram model without smoothing-------------")
    print(str)

def duplicates(lst,item):
    return [i for i, x in enumerate(lst) if x == item]

def sentence_generator(relational_probability,start_tag,end_tag):
    num=random.uniform(0, 1)
    str = ""
    temp_str = start_tag
    #v = relational_probability.get("s")
    #print(v[0][1])
    #print(relational_probability)
    while temp_str != end_tag:
        v = relational_probability.get(temp_str)[0][1]
        temp_str = random.choice(v).strip()
        #print(temp_str)
        if temp_str != end_tag:
            str += temp_str+" "

    print("-----------Random sentence from bigram model without smoothing-------------")
    print(str)



if __name__ == '__main__':
    input_file=sys.argv[1]
    start_tag=sys.argv[2]
    end_tag=sys.argv[3]

    probability_table= bigram(input_file)
    trigram(input_file)
    #create_relational_probability_table(probability_table,start_tag,end_tag)
    gen_sentence(probability_table,start_tag,end_tag)

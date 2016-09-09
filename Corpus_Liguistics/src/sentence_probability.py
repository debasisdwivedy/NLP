import nltk
import operator

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

    print_probility_table(probability_table_without_smoothing)

    print("------------------------")

    #Second Problem
    sen_list=sentence()
    token1=nltk.word_tokenize(''.join(sen_list))
    token=token+token1
    bigrm = nltk.bigrams(token)
    newmerator = nltk.FreqDist(bigrm)
    denominator=nltk.FreqDist(token)
    num_of_items=len(token)
    probability_table = addOneSmoothing(newmerator,denominator,num_of_items)
    print_probility_table(probability_table)
    print("------------------------")
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

    print_probility_table(probability_table)
    print("------------------------")
    # Second Problem
    sen_list = sentence()
    token1 = nltk.word_tokenize(''.join(sen_list))
    token = token + token1
    trigrm = nltk.trigrams(token)
    newmerator = nltk.FreqDist(trigrm)
    denominator = nltk.FreqDist(token)
    num_of_items = len(token)
    probability_table = addOneSmoothing(newmerator, denominator, num_of_items)
    print_probility_table(probability_table)
    print("------------------------")
    calculate_probability(probability_table, sen_list,"trigram")

    return probability_table

def sentence_generator(probability_table):
    relational_probability={}
    for k,v in probability_table.items():
        x = k[0]
        if x not in relational_probability:
            relational_probability[x]={}
        d = relational_probability[x]
        d[k[1]]=v
        relational_probability[x]=d
        #print(k,v)
    print("------------------------")
    for k,v in relational_probability.items():
        sorted_v = sorted(v.items(), key=operator.itemgetter(1))
        relational_probability[k] = sorted_v
    print_probility_table(relational_probability)


if __name__ == '__main__':
    probability_table= bigram()
    print("------------------------")
    #trigram()
    #print("------------------------")
    sentence_generator(probability_table)

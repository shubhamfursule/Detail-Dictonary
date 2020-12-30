def word_dict(word1):
    word_dict={}
    for i in word1:
        k=word1.count(i)
        word_dict.update({i:k})
    #print(word_dict)
    return word_dict
def char_dict(char1):
    char_dict={}
    for j in char1:
        x=char1.count(j)
        char_dict.update({j:x})
    #print(char_dict)
    return char_dict

def detail_dict(Sentence1,keys):
    countd,countU,countL,countv=0,0,0,0
    detail_d=dict.fromkeys(key,'non')
    a=[]
    b=[]

    for word in Sentence1.split():
        if word.isdigit():
            countd+=1
        a.append(word)
    detail_d['words']=word_dict(a)
    detail_d.update({'no of digits':countd})
    for char in Sentence:
        b.append(char)
        if char.isupper():
            countU+=1
        if char.islower():
            countL+=1           
        if char in "aeiou":
            countv+=1
            
    detail_d.update({'no. of vowels':countv})        
    detail_d.update({'no. of space characters':b.count(" ")}) 
    detail_d.update({'uppercase letter':countU})
    detail_d.update({'Characters':char_dict(b)})
    detail_d.update({'lowercase letter':countL})
    
    return detail_d
dict_d =detail_dict(Sentence,key)  
for keys,value in dict_d.items():
    print(keys , value )


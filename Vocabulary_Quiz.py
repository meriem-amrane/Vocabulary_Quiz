# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:38:45 2020

@author: ASUS
"""

import random
file = open("Vocabulary_list.csv","r")
wd_list = file.readlines()
print(wd_list)

wd_list.pop(0)
wd_set = set(wd_list)
file = open("Vocabulary_list.csv","w")
file.writelines(wd_set)

def get_word_and_definition(rawstring):
    word,definition = rawstring.split(',' ,1)
    return word,definition

def get_def_and_pop(word_list,word_dict):
    random_index=random.randrange(len(word_list))
    word=word_list.pop(random_index)
    definition=word_dict.get(word)
    return word, definition
word_dict =dict()
for rawstring in wd_set:
    word,definition = get_word_and_definition(rawstring)
    word_dict[word] =definition
    print(word)
#get a key from dictionary
while True:
    wd_list = list(word_dict)
    choice_list=[]
    for x in range(4):
        word,definition=get_def_and_pop(wd_list,word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)
    print(word)
    print("--------")

    for idx, choice in enumerate(choice_list):
        
        print(idx+1,choice)
    choice = int(input('Enter 1,2,3 or 4; 0 to exit:'))
    if choice_list[choice-1]==definition:
        print("corret")
    elif choice==0 :
        exit(0)
    else:
        print("incorrect")
        

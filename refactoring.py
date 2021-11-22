def pattern(string):
    import copy
    import re

    lst = list(string)
    list_of_numbers = tuple(map(str, range(10)))
    list_of_words = []

    i = 0
    while i < len(lst):
        #if element is a number
        if lst[i] in list_of_numbers:
            start = i
            while i < len(lst) and lst[i] in list_of_numbers:
                i += 1
            end = i
            list_of_words.append(''.join(lst[start:end]))
        #if element is a letter
        elif lst[i] != '\n' and lst[i] != ' ' and lst[i] != '\xa0':
            start = i
            while i < len(lst) and not(lst[i] in list_of_numbers) and lst[i] != '\n' and lst[i] != ' ' and lst[i] != '\xa0':
                i += 1
            end = i
            list_of_words.append(''.join(lst[start:end]))
            i += 1
        #if element is a ' ' or '\n' or '\xa0' 
        else:
            i += 1
    #then if there is a word merged with '...'
    
    return list_of_words

with open('test_file') as file:
    string = file.read()

print(pattern(string))
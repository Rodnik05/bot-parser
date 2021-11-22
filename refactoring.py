def split_into_words(string):
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
    i = 0
    while i < len(list_of_words):
        if '...' in list_of_words[i]:
            list_of_words.insert(i+1, '...')
            list_of_words.insert(i+1, list_of_words[i][:3])
            del list_of_words[i]
            i = i + 1
        i += 1    
    return list_of_words

def turn_into_date(list_of_words):
    list_of_numbers = tuple(map(str, range(10)))
    dict_of_dates = {}
    i = 0
    while i < len(list_of_words):
        if list_of_words[i][0] in list_of_numbers:
            if list_of_words[i-1] == 'До':
               pass
            #if word starts with a capital letter and it's not 'До'
            else:
                pass
        i += 1
    return dict_of_dates


with open('test_file') as file:
    string = file.read()

print(split_into_words(string))


def split_into_words(string) -> list:
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

def turn_into_date(list_of_words: str):
    list_of_numbers = tuple(map(str, range(10)))
    dict_of_dates = {}
    
#finding the first word with a capital letter and the first after
#so the sentence will be list[first_before : first_after]
def find_the_sentence(list_of_words: str, index: int):
    list_of_numbers = tuple(map(str, range(10)))
    i = index
    while i > 0:
        if list_of_words[i] == '...':
            i = i - 1
        elif list_of_words[i][0] in list_of_numbers:
            i = i - 1
        elif list_of_words[i].lower() == list_of_words[i]:
            i = i - 1
        elif list_of_words[i] == 'До':
            i = i - 1
        else: break
    first_before = i
    i = index
    while i < len(list_of_words):
        if list_of_words[i] == '...':
            i = i + 1
        elif list_of_words[i][0] in list_of_numbers:
            i = i + 1
        elif list_of_words[i].lower() == list_of_words[i]:
            i = i + 1
        else: break
    first_after = i
    return list_of_words[first_before: first_after]

def keep_only_dates(string: str):
    sentences_set = set()
    tuple_of_numbers = tuple(map(str, range(10)))
    i = 0
    while i < len(split_into_words(string)):
        elem = tuple(find_the_sentence(split_into_words(string), i))
        for x in tuple_of_numbers:
            if x in ''.join(elem):
                sentences_set.add(elem)
        i += 1

    return(sentences_set)


with open('test_file') as file:
    string = file.read()

print(keep_only_dates(string))

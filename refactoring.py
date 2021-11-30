def main(string):

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
            #if element is a ' ' or '\n' or '\xa0' 
            else:
                i += 1
        #then if there is a word merged with '...'
        i = 0
        while i < len(list_of_words):
            if '...' in list_of_words[i] and len(list_of_words[i]) != 3:
                list_of_words.insert(i+1, '...')
                list_of_words.insert(i+1, list_of_words[i][:3])
                del list_of_words[i]
                i = i + 1
            i += 1    
        return list_of_words
        
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

        return(tuple(sentences_set))
    
    def turn_into_date(sentences_set: set):
        list_of_numbers = tuple(map(str, range(10)))
        dict_of_dates = {}
        tuple_of_months = (
            'янв', 'фев', 'мар', 'апр', 
            'май', 'июн', 'июл', 'авг',
            'сен', 'окт', 'ноя', 'дек'
            )
        lst = []
        for x in sentences_set:
            i = 0
            start = 0
            while i < len(x):
                if x[i] in tuple_of_months:
                    if x[i-2] == 'До':
                        start = i - 2
                    elif x[i-2] == '...':
                        start = i - 3
                    else:
                        start = i - 1
                    break
                i += 1
            lst.append({' '.join(x[:start]) : x[start:]})
        return lst        
    res = turn_into_date(keep_only_dates(string))
    for l in res:
        for y in l:
            l[y] = (parser(l[y]))
    return res
    

def parser(tple: tuple):
    tuple_of_months = (
            'янв', 'фев', 'мар', 'апр', 
            'май', 'июн', 'июл', 'авг',
            'сен', 'окт', 'ноя', 'дек'
            )
    if tple[0] == 'До':
        #if 'До 12 дек'
        return tple[0], tple[1], tuple_of_months.index(tple[2]) + 1
    elif len(tple) == 2:
        #if '12 окт'
        return tple[0], tuple_of_months.index(tple[1]) + 1
    elif tple[1] == '...':
        #if '12 ... 13 дек'
        return (tple[0], tuple_of_months.index(tple[3]) + 1), \
            (tple[2], tuple_of_months.index(tple[3]) + 1)
    else:
        #if '12 дек ... 13 янв'
        return (tple[0], tuple_of_months.index(tple[1]) + 1), \
            (tple[3], tuple_of_months.index(tple[4]) + 1)
    

if __name__ == '__main__': 
    import requests 
    from bs4 import BeautifulSoup

    #keeping only text
    with open('test_file', 'w') as file:
        r = requests.get('https://olimpiada.ru/activity/99').text
        soup = BeautifulSoup(r, "lxml")
        message = soup.find("span", class_ ="classes_types_a").next_sibling.next_sibling.next_sibling.next_sibling.text
        file.write(message)

    with open('test_file') as file:
        string = file.read()
        
    res = main(string=string)
    print(res)
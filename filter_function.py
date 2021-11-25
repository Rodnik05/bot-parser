from typing import Tuple, Union, List
import json
import requests
from bs4 import BeautifulSoup
import threading
import refactoring

with open('olimpiads_list', 'r') as file:
    olimpiads_dict = json.load(file)

def get_by_id(ids: List[str], dict: dict = olimpiads_dict) -> dict:
    for id in ids:
        yield dict[id]

def get_by_level(dict: dict = olimpiads_dict, **kwargs) -> dict:
    level = kwargs['level']
    if 'id' in kwargs.keys():
        id = kwargs['id']
        yield [x for x in dict[id] if x['level'] == level]
    else:
        for id in dict:
            try:
                yield (x for x in dict[id] if x['level'] == level)
            except Exception as A:
                pass

def pull_date(url, message_list):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    message = soup.find("span", class_ ="classes_types_a").next_sibling.next_sibling.next_sibling.next_sibling.text
    result = not("Расписание олимпиады в этом году пока не известно" in message)
    if result:
        print(refactoring.main(message), sep=' ')
    print(url, result)
    if result:
        message_list.append(message)

def main():
    message_list = []
    pool = []
    for x in get_by_level(level='1'):
        for y in x:
            url = y['link']
            pool.append(threading.Thread(target=pull_date, args=(url,message_list)))

    for thread in pool:
        thread.start()
    for thread in pool:
        thread.join()
    
    return message_list

if __name__ == '__main__':
    main()
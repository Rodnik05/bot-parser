#importing required libraries
import requests
from bs4 import BeautifulSoup
from typing import Union, Optional, Tuple
import json

#turning the webpage file into a BeatifulSoup object
with open('webpage','r') as file:   
    webpage = file.read()
webpage = BeautifulSoup(webpage, "lxml")

#finding every id
id_list = []
for link in webpage.find('table', class_="note_table").find_all('a', class_='slim_dec'):
    id_list.append(link.get('href').split('#')[1])

#function that pulles the links
def link_puller(id: str, webpage: BeautifulSoup) -> Union[Tuple[Exception, str], list[Tuple[str, str, str]]]:
    try:
        list_of_olimpiads = []
        a = webpage.find("a", id=id).parent.parent.next_sibling.next_sibling
        for i in a.find_all("a", class_ = "slim_dec"):
            text = i.text.replace("\n", " ")
            newtext = text
            while True:
                text = newtext
                newtext = text.replace("  ", " ")
                if text == newtext: break
            list_of_olimpiads.append(
                dict([
                    ('link','https://olimpiada.ru' + i.get('href')), 
                    ('name',i.text), 
                    ('level',i.parent.parent.parent.td \
                    .next_sibling.next_sibling.next_sibling \
                    .next_sibling.next_sibling.next_sibling \
                    .text.replace("\n", "").replace("\n", ""))
                    ])
                )
        return list_of_olimpiads
    except BaseException as exception: 
        pass
        # return (exception, id)

big_dict = {}
for id in id_list:
    big_dict[id] = link_puller(id=id, webpage=webpage)


with open('olimpiads_list', 'w') as file:
    file.write(json.dumps(big_dict, ensure_ascii=False, indent=4))

from typing import Tuple, Union, List
import json

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
    for id in dict:
        try:
            yield (x for x in dict[id] if x['level'] == level)
        except Exception as A:
            print('\n', A,'\n', id)

for x in get_by_level(level='3'):
    for y in x:
        print(y)
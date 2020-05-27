import json


def data(filepath):
    with open(filepath, encoding='utf-8') as fr:
        result = json.load(fr)
    return result

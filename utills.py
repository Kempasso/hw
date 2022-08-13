import json


def load_candidates_from_json(path):  # возвращает список всех кандидатов
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def get_candidate(id, data):  # возвращает одного кандидата по его id
    for item in data:
        if item['id'] == id:
            return item


def get_candidates_by_name(candidate_name, data):  # возвращает кандидатов по имени
    arr = []
    for item in data:
        if item['name'].split(' ')[0] == candidate_name.capitalize():
            arr.append(item)
    return arr


def get_candidates_by_skill(skill_name, data):  # возвращает кандидатов по навыку
    arr = []
    for item in data:
        if skill_name.lower() in item['skills'].lower().split(', '):
            arr.append(item)
    return arr

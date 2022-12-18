import json


def load_candidates_from_json():
    """Возвращает список всех кандидатов"""
    with open('candidates.json', 'r', encoding="utf=8") as file:
        content = json.load(file)
    return content


def get_candidate(id):
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if id == candidate.get("id"):
            return candidate
    else:
        return "Нет такого кандидата"


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    all_candidate = []

    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate["name"].lower():
            all_candidate.append(candidate)
    if len(all_candidate) < 1:
        return "Нет такого кандидата"
    else:
        return all_candidate


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    all_candidates = []

    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            all_candidates.append(candidate)
    if len(all_candidates) < 1:
        return "Нет такого кандидата"
    else:
        return all_candidates

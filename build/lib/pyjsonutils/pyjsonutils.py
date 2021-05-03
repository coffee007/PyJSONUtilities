import json
from fuzzywuzzy import fuzz

def open_file_as_dict(file_path):
    d = {}
    try:
        json_file = open(file_path, "r")
        d = json.load(json_file)
        json_file.close()
    except:
        return None
    return d

def write_dict_to_file(d, file_path, indent=4):
    try:
        json_file = open(file_path, "w")
        json.dump(d, json_file, indent=4)
        json_file.close()
    except:
        return None

def update_json_file(file_path, new_dict, indent=4):
    try:
        k = open_file_as_dict(file_path)
        k.update(new_dict)
        write_dict_to_file(k, file_path)
    except: 
        return None

def find_key_from_value(d, value):
    for key in d:
        if d.get(key) == value:
            return key

def create_default_if_key_not_there(d, key, default_value = ""):
    if d.get(key) is None:
        d[key] = default_value
    return True

def pretty_print(d, indent=4):
    return json.dumps(d, indent=indent)
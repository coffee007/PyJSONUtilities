import json

def open_file_as_dict(path):
    file = open(path, "r")
    dict = json.load(file)
    file.close()
    return dict

def write_to_file(dict, path):
    file = open(path, "w")
    json.dump(dict, file)

class JSONFile:
    def __init__(self, path):
        self.path = path
        self.dict = open_file_as_dict(path)

    def write(self, path=self.path):
        write_to_file(self.dict, path)

    def find_key_from_value(self, value):
        for key, age in self.dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if key == value:
                return key

    def print_dict(self):
        print(self.dict)

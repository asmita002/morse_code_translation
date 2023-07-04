import json

#reads files and returns contents
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

#reads the json file and returns contents in the form of python dictionary
def read_json(file_path):
    return json.loads(read_file(file_path))


#translating plain text chars to morse code
def get_dict_keys_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value==target_value:
            return key
            
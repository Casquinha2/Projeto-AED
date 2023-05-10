import json
from View import *
class Controller:
    def __init__(self, master):
        self.view = View(master)
    
    def escrever_ficheiro_json(nome, d):
        json_string = json.dumps(d)
        json_file = open(nome, 'w')
        json_file.write(json_string)
        json_file.close()

    def ler_ficheiro_json(nome):
        with open(nome) as f:
            data = json.load(f)
        return data

    
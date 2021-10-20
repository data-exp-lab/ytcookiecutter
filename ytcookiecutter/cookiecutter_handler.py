import os
import json

def _check_file(filestr: str):
    if os.path.isfile(filestr) is False:
        raise FileNotFoundError(f"{filestr} not found.")

class CookieCutterHandler(dict):
    def __init__(self, json_file: str = "cookiecutter.json"):
        _check_file(json_file)
        self.json_file = json_file
        self.json_dict = self._load_json()

    def _load_json(self):
        with open(self.json_file, "r") as jfi:
            jdict = json.load(jfi)
        return jdict

    def json_dump(self):
        with open(self.json_file, "w") as jfi:
            json.dump(self.json_dict, jfi, indent=2)


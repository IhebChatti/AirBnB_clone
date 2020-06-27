#!/usr/bin/python3
from os import path
import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        _id = obj.id
        key = str(obj.__class__.__name__) + "." + _id
        FileStorage.__objects[key] = obj

    def save(self):
        dct = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            for k, v in FileStorage.__objects.items():
                dct[k] = v.to_dict()
            json.dump(dct, f)

    def reload(self):
        from models.base_model import BaseModel
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj = json.load(f)
                dct = {}
                for k, v in obj.items():
                    dct[k] = BaseModel(**v)
                FileStorage.__objects = dct
        else:
            return

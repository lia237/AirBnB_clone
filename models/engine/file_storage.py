import json
from os import path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.____name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, obj in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**obj)

# Create a unique FileStorage instance
storage = FileStorage()
storage.reload()


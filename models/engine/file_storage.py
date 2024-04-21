#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        filtered_objs = {}
        for obj_id, obj in self.__objects.items():
            if obj_id.strip('.')[0] == cls_name:
                filtered_objs[obj_id] = obj
        return filtered_objs
        """
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            my_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    my_dict[key] = value
            return my_dict
        return self.__objects
        """

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity

        myClasses = [BaseModel, User, Place, City, Review, State, Amenity]

        def serialize(obj):
            for myClass in myClasses:
                if isinstance(obj, myClass):
                    return obj.to_dict()
            return obj

        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file, default=serialize)

        """
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it's inside"""
        if obj is not None:
            for key, value in FileStorage.__objects.items():
                if isinstance(value, type(obj)) and value == obj:
                    del FileStorage.__objects[key]
                    break

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            storage.new(self)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        dic = self.__dict__.copy()
        dic.pop("_sa_instance_state", None)
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        # return '[{}] ({}) {}'.format(cls, self.id, dic)
        my_str = f"[{self.__class__.__name__}] ({self.id}) {dic}"

        return my_str

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': (str(type(self)).split('.')
                          [-1]).split('\'')[0]})

        if '_sa_instance_state' in dictionary.keys():
            dictionary.pop('_sa_instance_state', None)

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)

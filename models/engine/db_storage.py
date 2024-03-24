#!/usr/bin/python3
"""Module contains class DBStorage for database storage engine"""
import os
from datetime import datetime
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiation method to create engine for each instance"""
        uri = "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')
                )

        self.__engine = create_engine(uri, pool_pre_ping=True)
        # Base.metadata.create_all(self.__engine)

        if os.getenv('HBNB_ENV') == 'test':
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects on the current database session base on cls"""
        obj_dictionary = {}
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dictionary[key] = obj

        return obj_dictionary

    def new(self, obj):
        """add the object to the current database session"""
        if self.__session is None:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        if self.__session is not None:
            self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None"""
        if obj is not None and self.__session is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all tables in the database"""

        # create all tables in the database
        Base.metadata.create_all(self.__engine)

        # create a new session with sessionmaker
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Closes the session"""
        self.__session.close()

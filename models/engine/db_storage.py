#!/usr/bin/python3
"""Module contains class DBStorage for database storage engine"""
import os
from datetime import datetime
from models.base_model import BaseModel, Base
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
        Base.metadata.create_all(self.__engine)

        if os.getenv('HBNB_ENV') == 'test':
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects on the current database session base on cls"""
        if self.__session is None:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

        obj_dictionary = {}
        if cls is None:
            objs = self.__session.query(Base).all()
        else:
            if isinstance(cls, str):
                cls = globals().get(cls)
            objs = self.__session.query(cls).all()

        for obj in objs:
            dictionary = {}
            for column in obj.__mapper__.columns:
                value = getattr(obj, column.name)
                # Convert datetime objects to ISO format
                if isinstance(value, datetime):
                    value = value.isoformat()
                dictionary[column.name] = value
            # Add class name to the dictionary
            dictionary['__class__'] = type(obj).__name__
            # Use object id as dictionary key
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dictionary[key] = dictionary

            """
            key = "{}.{}".format(obj.to_dict()['__class__'], obj.id)
            value = obj
            obj_dictionary[key] = value
            """

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
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # create all tables in the database
        Base.metadata.create_all(self.__engine)

        # create a new session with sessionmaker
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

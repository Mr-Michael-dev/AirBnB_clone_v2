#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
            """
            related_cities = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities

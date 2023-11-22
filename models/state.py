#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), primary_key=True, nullable=False)

    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """Getter for all cities assocaited with state"""
        from models.city import City
        from models import storage
        city_list = []
        cities_all = storage.all(City)
        for city in cities_all:
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

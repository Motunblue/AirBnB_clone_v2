#!/usr/bin/python3
"""Module defines storage for Database storage"""
from sqlalchemy import (create_engine)
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Data base storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Instatiation method of Database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'), os.environ.get(
                'HBNB_MYSQL_PWD'), os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadate.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """Query the current datatbase session"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                k = f"{obj.__class__.__name__}.{obj.id}"
                dict[k] = obj
        else:
            cls_list = [State, City, User, Place, Review, Amenity]
            for c in cls_list:
                objs = self.__session.query(c).all()
                for obj in objs:
                    k = f"{obj.__class__.__name__}.{obj.id}"
                    dict[k] = obj

        return dict

    def new(self, obj):
        """Adds new object to the Database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes in current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes and object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the DB"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(Session)

    def close(self):
        """Remove session"""
        self.__session.remove()

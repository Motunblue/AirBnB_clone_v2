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
        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'), os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'), os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)

        #if os.environ.get('HBNB_ENV') == 'test':
            #Base.metadate.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """Query the current datatbase session"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dict = {}
        if cls:
            objs =  DBStorage.__session.query(cls).all()
            for obj in objs:
                k = f"{obj.__class__.__name__}.{obj.id}"
                dict[k] = obj
        else:
            cls_list = [State, City]
            for c in cls_list:
                objs =  DBStorage.__session.query(c).all()
                for obj in objs:
                    k = f"{obj.__class__.__name__}.{obj.id}"
                    dict[k] = obj
                
        return dict
    
    def new(self, obj):
        """Adds new object to the Database"""
        type(self).__session.add(obj)
    
    def save(self):
        """Commit all changes in current session"""
        type(self).__session.commit()

    def delete(self, obj=None):
        """Deletes and object"""
        if obj:
            type(self).__session.delete(obj)
        self.save()

    def reload(self):
        """Creates all tables in the DB"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(DBStorage.__engine) #make sure all classes are imported
        Session = sessionmaker(bind=DBStorage.__engine, expire_on_commit=False)

        DBStorage.__session =  scoped_session(Session)


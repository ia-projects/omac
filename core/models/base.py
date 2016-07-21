"""
Base clases for persistance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Engine:

    def __init__(self, engine, path, reset_db=False):
        # Create an engine that stores data in the local directory's
        # sqlalchemy_example.db file.
        db_engine = '{}://{}'.format(engine, path)
        self._engine = create_engine(db_engine)
        self._DBSession = sessionmaker(self._engine)


        # Create all tables in the engine. This is equivalent to "Create Table"
        # statements in raw SQL.
        if reset_db:
            Base.metadata.create_all(self._engine)

    @property
    def session(self): return self._DBSession
# Libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Env
from config.env import Env


# CONNECTION
''' Components [Interact with SQL]
    => Engine:  allows to manage Tables on SQL DB [can be used ALEMBIC LIB for Migrations Online and Offline]

    => Session: allows to interact with SQL DB [CRUD]
                Transactions:
                - .add()        - .query()
                - .commit()     - .refresh()

    Components [Interact with Python]
    => Base  :  <class> that can have <subclasses> which are
                the <modeltype tables> [created in models.py]
                to be used as <<Object Reference>> in
                - Engine    =>      Table Creation
                - Session   =>      Table DataContent [CRUD]
'''
engine = create_engine(Env("DB_DSN"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

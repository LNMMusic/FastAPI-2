# Libaries
from sqlalchemy     import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# DB
from db.database    import Base
# SECURITY
from config.pswd    import pwd_context
# DESCRIPTION
''' This file manage Tables Creation of SQL with db_models for User Settings '''


# TABLES [Models]
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Field for access to all its other Tables
    items = relationship("Item", back_populates="owner")

    # METHODS [Security]
    def verify_password(self, password:str):
        return pwd_context.verify(password, self.hashed_password)

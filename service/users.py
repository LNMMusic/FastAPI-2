# LIBRARIES
# TYPES
from fastapi import Depends
import schema, model
# DB
from db.session  import get_db


# CRUD
def get_user(username: str, db) -> model.User:
    return db.query(model.User).filter(model.User.username == username).first()

def create_user(user: schema.UserAuth, db) -> schema.User.from_orm:
    # Creation
    db_user = model.User(
        username = user.username,
        email    = user.email,
        password = user.password
    )
    db_user.password_hashing()

    # Save
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Return
    return schema.User.from_orm(db_user)


# VALIDATIONS
def valid_user_signup(username: str, db) -> bool:
    db_user = get_user(username, db)
    if db_user:
        return False
    return True

def valid_user_login(db_user: model.User, password: str) -> bool:
    if db_user is None:
        return False
    if not db_user.password_validation(password):
        return False
    return True
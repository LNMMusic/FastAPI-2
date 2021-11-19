# LIBRARIES
# TYPES
import schema, model
# DB
from db.session  import get_db


# CRUD
def get_user(username: str) -> model.User:
    return db.query(model.User).filter(model.User.username == username).first()

def create_user(user: schema.UserCreate) -> schema.User.from_orm:
    # Response
    db = get_db()
    db_user = model.User()

    # Creation
    if get_user(user.username):
        return db_user
    
    db_user.username = user.username
    db_user.email    = user.email
    db_user.password = user.password;   db_user.password_hashing()

    # Save
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Return
    return schema.User.from_orm(db_user)

from db.connection import SessionLocal

def get_db():
    ''' create session on sql [transactions] '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import Column, String, Integer, Enum, Date
from app import app, db
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime


create_engine('sqlite:///kanban.db', echo=True)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    status = Column(Enum('to_do', 'doing', 'done'))
    date = Column(Date, default=datetime.utcnow)



# Initialize database
with app.app_context():
    Base.metadata.create_all(db.engine)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Table1(Base):
    __tablename__ = 'Table1'
    #__tablename__ = 'table1'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Add methods for creating, updating, and deleting records (optional)

# Create a session maker object (optional for this example)
# Engine connection details moved to app.py
# Session = sessionmaker(bind=engine)

    def get_record_by_id(id):
        return Table1.query.get(id)

    def create_record(data):
        new_record = Table1(name=data['name'], email=data['email'])
        db.session.add(new_record)
        db.session.commit()

    def update_record(id, data):
        record = get_record_by_id(id)
        if record:
            record.name = data['name']
            record.email = data['email']
            db.session.commit()

    def delete_record(id):
        record = get_record_by_id(id)
    def create_record(data):
    new_record = Table1(name=data['name'], email=data['email'])
    db.session.add(new_record)
    db.session.commit()

    def update_record(id, data):
        record = get_record_by_id(id)
        if record:
            record.name = data['name']
            record.email = data['email']
            db.session.commit()

    def delete_record(id):
        record = get_record_by_id(id)
        if record:
            db.session.delete(record)
            db.session.commit()





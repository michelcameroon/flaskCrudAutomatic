from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school1.db'
db = SQLAlchemy(app)

# Import the Table1 model
from models import Table1

# Create the database tables (if they don't already exist)
##db.create_all()

# Example functions for CRUD operations
def get_all_records():
    return Table1.query.all()
'''
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
    if record:
        db.session.delete(record)
        db.session.commit()
'''

@app.route('/')
def list_records():
    with app.app_context():
        db.create_all()
        #records = get_all_records()
        print ('Table1=')
        print (Table1)
        records = Table1.query.all()
    return render_template('list.html', records=records)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_record_form(id):
    record = get_record_by_id(id)
    if request.method == 'POST':
        update_record(id, request.form)
        return redirect(url_for('list_records'))
    return render_template('update.html', record=record)

@app.route('/create', methods=['GET', 'POST'])
def create_record_form():
    if request.method == 'POST':
        create_record(request.form)
        return redirect(url_for('list_records'))
    return render_template('create.html')

@app.route('/delete/<int:id>')
def delete_record(id):
    delete_record(id)
    return redirect(url_for('list_records'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

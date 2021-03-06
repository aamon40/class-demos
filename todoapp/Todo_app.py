from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/postgres'
db = SQLAlchemy(app)

migrate = Migrate(app, db)



class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Task ID: {self.id}, description: {self.description}>'

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.data.get('description', '')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()

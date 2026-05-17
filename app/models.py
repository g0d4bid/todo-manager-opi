from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class TaskModel(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.String(20), default='Medium', nullable=False)
    due_date = db.Column(db.String(20), nullable=True)
    category = db.Column(db.String(50), default='General', nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)


class Employee(db.Model):
    __tablename__ = 'employees'  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    membership = db.Column(db.String(100), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    netpay = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Employee {self.name}>"

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Association table for many-to-many relationship between User and Technician
user_technician = db.Table('user_technician',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    appointments = db.relationship('Appointment', backref='user', lazy=True)
    technicians = db.relationship('Technician',
                                   secondary=user_technician,
                                   backref=db.backref('users', lazy=True))

class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    appointments = db.relationship('Appointment', backref='technician', lazy=True)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000), nullable=True)

class Appointment(db.Model):
    __tablename__ = 'appointment'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    service = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    history_entries = db.relationship('AppointmentHistory', backref='appointment', lazy=True)

class AppointmentHistory(db.Model):
    __tablename__ = 'appointment_history'
    
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # e.g., 'Created', 'Updated', 'Cancelled'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    # Relationships to User and Technician (if needed)
    user = db.relationship('User', backref='appointment_histories', lazy=True)
    technician = db.relationship('Technician', backref='appointment_histories', lazy=True)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for many-to-many relationship between User and Technician
user_technician_assignments = db.Table('user_technician_assignments',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('technician_id', db.Integer, db.ForeignKey('technicians.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    appointments = db.relationship('Appointment', backref='user', lazy=True)
    technicians = db.relationship('Technician', secondary=user_technician_assignments, backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.id'), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"Appointment('{self.date}', '{self.status}')"

class Technician(db.Model):
    __tablename__ = 'technicians'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    appointments = db.relationship('Appointment', backref='technician', lazy=True)

    def __repr__(self):
        return f"Technician('{self.name}', '{self.email}')"

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"Inventory('{self.item_name}', '{self.quantity}')"
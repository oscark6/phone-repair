from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
import os
import re
from config import Config
from models import db, User, Appointment, Technician, Inventory

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)
CORS(app)

# Root route
@app.route('/')
def home():
    return "Welcome to the Phone Repair Service API"

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None



# RESTful resources
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Username, email, and password are required'}), 400

    if not validate_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    if len(data['password']) < 6:
        return jsonify({'message': 'Password must be at least 6 characters long'}), 400

    # Check if user or email already exists
    existing_user = User.query.filter((User.username == data['username']) | (User.email == data['email'])).first()
    if existing_user:
        return jsonify({'message': 'Username or email already exists'}), 409

    # Hash the password
    hashed_password = generate_password_hash(data['password'])

    # Create a new user instance
    new_user = User(
        username=data['username'], 
        email=data['email'], 
        password=hashed_password,
        role='user'  # Provide a default role if not specified
    )

    # Add new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Generate access token
    access_token = create_access_token(identity={'username': new_user.username, 'role': new_user.role})
    
    return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400

    # Query the user
    user = User.query.filter_by(username=data['username']).first()

    # Check if user exists and password matches
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    # Create access token
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify({'access_token': access_token}), 200

class AppointmentResource(Resource):
    @jwt_required()
    def get(self, id):
        appointment = Appointment.query.get(id)
        if not appointment:
            return {'error': 'Appointment not found'}, 404
        return {
            'id': appointment.id,
            'user_id': appointment.user_id,
            'technician_id': appointment.technician_id,
            'date': appointment.date,
            'status': appointment.status,
            'description': appointment.description
        }
    
    @jwt_required()
    def put(self, id):
        data = request.get_json()
        appointment = Appointment.query.get(id)
        if not appointment:
            return {'error': 'Appointment not found'}, 404
        appointment.date = data['date']
        appointment.status = data['status']
        appointment.description = data['description']
        db.session.commit()
        return {'message': 'Appointment updated successfully'}
    
    @jwt_required()
    def delete(self, id):
        appointment = Appointment.query.get(id)
        if not appointment:
            return {'error': 'Appointment not found'}, 404
        db.session.delete(appointment)
        db.session.commit()
        return {'message': 'Appointment deleted successfully'}

class AppointmentListResource(Resource):
    @jwt_required()
    def get(self):
        appointments = Appointment.query.all()
        return [{'id': appt.id, 'user_id': appt.user_id, 'technician_id': appt.technician_id, 'date': appt.date, 'status': appt.status} for appt in appointments]
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        new_appointment = Appointment(
            user_id=data['user_id'],
            technician_id=data['technician_id'],
            date=data['date'],
            status=data['status'],
            description=data['description']
        )
        db.session.add(new_appointment)
        db.session.commit()
        return {'message': 'Appointment created successfully', 'id': new_appointment.id}

class InventoryResource(Resource):
    @jwt_required()
    def get(self):
        items = Inventory.query.all()
        return [{'id': item.id, 'item_name': item.item_name, 'quantity': item.quantity, 'price': item.price, 'description': item.description} for item in items]
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        new_item = Inventory(
            item_name=data['item_name'],
            quantity=data['quantity'],
            price=data['price'],
            description=data['description']
        )
        db.session.add(new_item)
        db.session.commit()
        return {'message': 'Item added to inventory', 'id': new_item.id}

# api.add_resource(Register, '/register')
# api.add_resource(Login, '/login')
api.add_resource(AppointmentResource, '/appointments/<int:id>')
api.add_resource(AppointmentListResource, '/appointments')
api.add_resource(InventoryResource, '/inventory')

if __name__ == '__main__':
    app.run(debug=True)

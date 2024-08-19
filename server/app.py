from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_migrate import Migrate
import re
from datetime import datetime
from models import db, User, Appointment, Inventory, AppointmentHistory  # Import models from your separate file

# Configuration
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///repair_shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret_key'

# Initialize Flask app and extensions
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# Utility functions
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Routes
@app.route('/')
def home():
    return "Welcome to the Phone Repair Service API"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Username, email, and password are required'}), 400
    if not validate_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400
    if len(data['password']) < 6:
        return jsonify({'message': 'Password must be at least 6 characters long'}), 400
    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return jsonify({'message': 'Username or email already exists'}), 409

    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], email=data['email'], password=hashed_password, role='user')
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity={'username': new_user.username, 'role': new_user.role})
    return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing email or password'}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify({'access_token': access_token}), 200


@app.route('/appointments/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def manage_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({'error': 'Appointment not found'}), 404

    if request.method == 'GET':
        return jsonify({
            'id': appointment.id,
            'user_id': appointment.user_id,
            'technician_id': appointment.technician_id,
            'date': appointment.date.isoformat(),
            'status': appointment.status,
            'description': appointment.description
        })

    if request.method == 'PUT':
        data = request.get_json()
        appointment.date = datetime.fromisoformat(data['date'])
        appointment.status = data['status']
        appointment.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Appointment updated successfully'})

    if request.method == 'DELETE':
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'})

@app.route('/appointments', methods=['POST'])
# @jwt_required()
def create_appointment():
    data = request.get_json()
    # print("Received Data:", data)  # Log the received data

    # Check for required fields
    if not all(field in data for field in ['date', 'service','user_id','technician_id','status', 'description']):
        return jsonify({'msg': 'Missing required fields'}), 422

    try:
        print("Please service", data['service'])
        # Get the current user ID from the JWT
        # current_user_id = get_jwt_identity()
        # print("Current User ID:", current_user_id)  # Log the current user ID
        
        # Logic to assign a technician
        # technician_id = 1  # Replace with actual logic
        # print("Assigned Technician ID:", technician_id)  # Log the assigned technician ID

        # Attempt to create a new appointment
        new_appointment = Appointment(
            user_id=data["user_id"],
            description=data['description'],
            technician_id=data['technician_id'],
            date=datetime.fromisoformat(data['date']),
            service=data['service'],
            status=data['status']
        )


        print("\n================================", new_appointment)
        db.session.add(new_appointment)
        db.session.commit()
        print("New Appointment Created:", new_appointment.id)  # Log the new appointment ID

        # Create the appointment history entry
        history_entry = AppointmentHistory(
            appointment_id=new_appointment.id,
            user_id=new_appointment.user_id,
            technician_id=new_appointment.technician_id,
            action='Created',
            status=new_appointment.status,
            description=new_appointment.description
        )
        db.session.add(history_entry)
        db.session.commit()

        return jsonify({'message': 'Appointment created successfully', 'id': new_appointment.id}), 201

    except Exception as e:
        db.session.rollback()
        print("Error during appointment creation:", str(e))  # Log the error message
        return jsonify({'msg': str(e)}), 500
@app.route('/appointments/history', methods=['GET'])
@jwt_required()
def get_history():
    try:
        history_entries = AppointmentHistory.query.all()
        result = [{
            'id': entry.id,
            'appointment_id': entry.appointment_id,
            'user_id': entry.user_id,
            'technician_id': entry.technician_id,
            'action': entry.action,
            'timestamp': entry.timestamp.isoformat(),
            'status': entry.status,
            'description': entry.description
        } for entry in history_entries]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/inventory', methods=['GET', 'POST'])
@jwt_required()
def manage_inventory():
    if request.method == 'GET':
        items = Inventory.query.all()
        return jsonify([{
            'id': item.id,
            'item_name': item.item_name,
            'quantity': item.quantity,
            'price': item.price,
            'description': item.description
        } for item in items])

    if request.method == 'POST':
        data = request.get_json()
        new_item = Inventory(
            item_name=data['item_name'],
            quantity=data['quantity'],
            price=data['price'],
            description=data['description']
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added to inventory', 'id': new_item.id}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

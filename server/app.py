from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os
from config import DevelopmentConfig
from models import db, User, Appointment, Technician, Inventory

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

# Root route
@app.route('/')
def home():
    return "Welcome to the Phone Repair Service API"

# RESTful resources
class Register(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role='user'  # Default role
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully'}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username'], password=data['password']).first()
        if not user:
            return {'message': 'Invalid credentials'}, 401
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return {'access_token': access_token}, 200

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

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(AppointmentResource, '/appointments/<int:id>')
api.add_resource(AppointmentListResource, '/appointments')
api.add_resource(InventoryResource, '/inventory')

if __name__ == '__main__':
    app.run(debug=True)
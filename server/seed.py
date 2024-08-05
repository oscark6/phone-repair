# Import necessary modules
from app import app, db
from models import User, Technician, Inventory
from faker import Faker
import random

# Define constants
NUM_SAMPLE_RECORDS = 20
MIN_PRICE = 10.0
MAX_PRICE = 500.0

# Initialize Faker instance
fake = Faker()

def add_sample_data():
    """
    Add sample data to the database.
    """
    # Add sample users
    if not User.query.first():
        users = [
            User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                role=random.choice(['user', 'admin'])
            ) for _ in range(NUM_SAMPLE_RECORDS)
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()

    # Add sample technicians
    if not Technician.query.first():
        specialties = [
            'Screen Repair',
            'Battery Replacement',
            'Software Issues',
            'General Maintenance',
            'Hardware Repair',
            'Data Recovery'
        ]
        technicians = [
            Technician(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                specialty=random.choice(specialties)
            ) for _ in range(NUM_SAMPLE_RECORDS)
        ]
        db.session.bulk_save_objects(technicians)
        db.session.commit()

    # Add sample inventory items
    if not Inventory.query.first():
        inventory_items = [
            Inventory(
                item_name=f"{fake.word().capitalize()} {fake.word().capitalize()}",
                quantity=random.randint(1, 100),
                price=round(random.uniform(MIN_PRICE, MAX_PRICE), 2),
                description=fake.sentence()
            ) for _ in range(NUM_SAMPLE_RECORDS)
        ]
        db.session.bulk_save_objects(inventory_items)
        db.session.commit()

# Create database tables and add sample data
with app.app_context():
    db.create_all()
    add_sample_data()
from app import app, db
from models import User, Technician, Inventory
from faker import Faker
import random

fake = Faker()

def add_sample_data():
    # Add sample users
    if not User.query.first():
        users = []
        for _ in range(20):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                role=random.choice(['user', 'admin'])
            )
            users.append(user)
        db.session.bulk_save_objects(users)
        db.session.commit()

    # Add sample technicians
    if not Technician.query.first():
        technicians = []
        for _ in range(20):
            technician = Technician(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                specialty=random.choice(['Screen Repair', 'Battery Replacement', 'Software Issues', 'General Maintenance', 'Hardware Repair', 'Data Recovery'])
            )
            technicians.append(technician)
        db.session.bulk_save_objects(technicians)
        db.session.commit()

    # Add sample inventory items
    if not Inventory.query.first():
        inventory_items = []
        for _ in range(20):
            item_name = f"{fake.word().capitalize()} {fake.word().capitalize()}"
            inventory_item = Inventory(
                item_name=item_name,
                quantity=random.randint(1, 100),
                price=round(random.uniform(10.0, 500.0), 2),
                description=fake.sentence()
            )
            inventory_items.append(inventory_item)
        db.session.bulk_save_objects(inventory_items)
        db.session.commit()

with app.app_context():
    db.create_all()
    add_sample_data()

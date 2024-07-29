from app import app, db
from models import User, Technician, Inventory

with app.app_context():
    db.create_all()

    # Add some sample data
    if not User.query.first():
        user1 = User(username='john_doe', email='john@example.com', password='password', role='user')
        db.session.add(user1)
        db.session.commit()

    if not Technician.query.first():
        tech1 = Technician(name='Jane Smith', email='jane@example.com', phone='555-5555', specialty='Screen Repair')
        db.session.add(tech1)
        db.session.commit()

    if not Inventory.query.first():
        item1 = Inventory(item_name='iPhone Screen', quantity=10, price=99.99, description='Replacement screen for iPhone')
        db.session.add(item1)
        db.session.commit()

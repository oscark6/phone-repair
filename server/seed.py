from models import db, User, Technician, Inventory

def seed_data():
    # Create admin user
    admin_user = User(username='admin', email='admin@example.com', password='password', role='admin')
    db.session.add(admin_user)

    # Create technicians
    technician1 = Technician(name='John Doe', email='john@example.com')
    technician2 = Technician(name='Jane Doe', email='jane@example.com')
    db.session.add(technician1)
    db.session.add(technician2)

    # Create inventory items
    item1 = Inventory(item_name='iPhone Screen', quantity=10, price=50.0, description='iPhone screen replacement')
    item2 = Inventory(item_name='Samsung Battery', quantity=20, price=30.0, description='Samsung battery replacement')
    db.session.add(item1)
    db.session.add(item2)

    # Commit changes
    db.session.commit()

if __name__ == '__main__':
    seed_data()
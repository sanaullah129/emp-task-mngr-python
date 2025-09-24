from database import SessionLocal, engine
from models import Base, User, Employee, Task, TaskStatus
from auth import get_password_hash
from datetime import datetime, timedelta

def init_db():
    """Initialize the database and create tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def seed_data():
    """Seed the database with initial data"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("Database already has data. Skipping seed operation.")
            return
        
        print("Seeding database with initial data...")
        
        # Create a test user
        test_user = User(
            username="admin",
            hashed_password=get_password_hash("admin123")
        )
        db.add(test_user)
        
        # Create sample employees
        employees = [
            Employee(
                name="John Doe",
                email="john.doe@company.com",
                department="Engineering",
                position="Software Developer"
            ),
            Employee(
                name="Jane Smith",
                email="jane.smith@company.com",
                department="Marketing",
                position="Marketing Manager"
            ),
            Employee(
                name="Mike Johnson",
                email="mike.johnson@company.com",
                department="Engineering",
                position="Senior Developer"
            ),
            Employee(
                name="Sarah Wilson",
                email="sarah.wilson@company.com",
                department="HR",
                position="HR Specialist"
            )
        ]
        
        for employee in employees:
            db.add(employee)
        
        db.commit()
        
        # Create sample tasks
        tasks = [
            Task(
                title="Implement user authentication",
                description="Create JWT-based authentication system",
                status=TaskStatus.ongoing,
                due_date=datetime.utcnow() + timedelta(days=7),
                employee_id=1  # John Doe
            ),
            Task(
                title="Design marketing campaign",
                description="Create Q4 marketing campaign for new product launch",
                status=TaskStatus.pending,
                due_date=datetime.utcnow() + timedelta(days=14),
                employee_id=2  # Jane Smith
            ),
            Task(
                title="Code review process setup",
                description="Establish code review guidelines and process",
                status=TaskStatus.completed,
                due_date=datetime.utcnow() - timedelta(days=3),
                employee_id=3  # Mike Johnson
            ),
            Task(
                title="Employee handbook update",
                description="Update employee handbook with new policies",
                status=TaskStatus.pending,
                due_date=datetime.utcnow() + timedelta(days=10),
                employee_id=4  # Sarah Wilson
            ),
            Task(
                title="Database optimization",
                description="Optimize database queries for better performance",
                status=TaskStatus.ongoing,
                due_date=datetime.utcnow() + timedelta(days=5),
                employee_id=1  # John Doe
            )
        ]
        
        for task in tasks:
            db.add(task)
        
        db.commit()
        
        print("Database seeded successfully!")
        print("\nTest credentials:")
        print("Username: admin")
        print("Password: admin123")
        print(f"\nCreated {len(employees)} employees and {len(tasks)} tasks")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing Employee Task Manager Database...")
    init_db()
    seed_data()
    print("Database setup completed!")
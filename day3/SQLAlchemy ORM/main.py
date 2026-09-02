from database import Base, engine, SessionLocal
from models import User, Post

# Create tables
Base.metadata.create_all(bind=engine)

def run_demo():
    db = SessionLocal()

    # Create User
    new_user = User(name="Krishna", email="krishna@example.com")
    db.add(new_user)
    db.commit()

    # Create Post with relationship
    new_post = Post(title="ORM Integration", content="SQLAlchemy Done", user_id=new_user.id)
    db.add(new_post)
    db.commit()

    # Query with relationship
    user = db.query(User).filter(User.id == new_user.id).first()
    print(f"User: {user.name} - Posts: {len(user.posts)}")
    db.close()

if __name__ == "__main__":
    run_demo()
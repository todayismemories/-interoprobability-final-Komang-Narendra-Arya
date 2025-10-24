# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database akan berada di folder backend/ dengan nama campus_events.db
DATABASE_URL = "sqlite:///./campus_events.db"

engine = create_engine(
    DATABASE_URL, 
    # 'connect_args' wajib untuk SQLite + FastAPI
    connect_args={"check_same_thread": False} 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 'Base' ini akan diimpor oleh model.py
Base = declarative_base()

# Fungsi untuk dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# backend/model.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

# --- PERBAIKAN IMPORT (Tanpa tanda '.') ---
from database import Base 
# -------------------------------------------

# Tabel 1: events (Tugas 1)
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100))
    date = Column(Date)
    location = Column(String(100))
    quota = Column(Integer)
    
    # Relasi ke Participant
    participants = relationship("Participant", back_populates="event")

# Tabel 2: participants (Tugas 3)
class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    event_id = Column(Integer, ForeignKey("events.id"))
    
    # Relasi ke Event
    event = relationship("Event", back_populates="participants")
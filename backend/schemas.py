# backend/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import List, Optional

# --- Schemas untuk Participant (Tugas 3) ---
class ParticipantBase(BaseModel):
    name: str
    email: str
    event_id: int

class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id: int
    class Config:
        from_attributes = True # Perbaikan dari 'orm_mode'

# --- Schemas untuk Event (Tugas 2) ---
class EventBase(BaseModel):
    title: str
    date: date
    location: str
    quota: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    class Config:
        from_attributes = True # Perbaikan dari 'orm_mode'

# --- Skema 'User' dan 'Token' dihapus untuk menyederhanakan ---
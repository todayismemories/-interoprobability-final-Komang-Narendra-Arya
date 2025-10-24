# backend/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional 

# (PENTING) Impor CORS untuk Interoperabilitas
from fastapi.middleware.cors import CORSMiddleware

# --- PERBAIKAN IMPORT (Tanpa tanda '.') ---
import model
import schemas
import database
from database import engine, get_db, Base
# -------------------------------------------

# Perintah ini membuat tabel (events & participants) di database Anda
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Campus Event API (UTS)",
    description="Proyek ini memenuhi Tugas 1, 2, 3, 4, dan 6 (Bonus Dokumentasi)."
)

# --- KONFIGURASI CORS ---
# (Wajib agar frontend/index.html bisa mengakses backend ini)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Mengizinkan semua origin
    allow_credentials=True,
    allow_methods=["*"], # Mengizinkan semua metode (GET, POST, etc.)
    allow_headers=["*"], # Mengizinkan semua header
)
# -------------------------

# --- Semua kode Autentikasi (Tugas 5) dihapus ---


# === TUGAS 2: Implementasi CRUD untuk Event ===
# (Endpoint ini sekarang publik, tidak dilindungi token)

@app.get("/events", response_model=List[schemas.Event], tags=["Events"])
def get_all_events(db: Session = Depends(get_db)):
    events = db.query(model.Event).all()
    return events

@app.post("/events", response_model=schemas.Event, status_code=201, tags=["Events"])
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = model.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@app.put("/events/{id}", response_model=schemas.Event, tags=["Events"])
def update_event(id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = db.query(model.Event).filter(model.Event.id == id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db_event.title = event.title
    db_event.date = event.date
    db_event.location = event.location
    db_event.quota = event.quota
    
    db.commit()
    db.refresh(db_event)
    return db_event

@app.delete("/events/{id}", response_model=dict, tags=["Events"])
def delete_event(id: int, db: Session = Depends(get_db)):
    db_event = db.query(model.Event).filter(model.Event.id == id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
        
    db.delete(db_event)
    db.commit()
    return {"message": "Event deleted successfully"}

# === TUGAS 3: Pendaftaran Peserta (Participants) ===

@app.post("/register", response_model=schemas.Participant, status_code=201, tags=["Participants"])
def register_participant(participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    db_event = db.query(model.Event).filter(model.Event.id == participant.event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
        
    db_participant = model.Participant(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

@app.get("/participants", response_model=List[schemas.Participant], tags=["Participants"])
def get_all_participants(db: Session = Depends(get_db)):
    participants = db.query(model.Participant).all()
    return participants
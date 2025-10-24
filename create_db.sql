/* create_db.sql (VERSI UNTUK SQLite - Sederhana) */

/* Tabel 1: events (Sesuai Struktur di UTS) */
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    date DATE,
    location VARCHAR(100),
    quota INTEGER
);

/* Tabel 2: participants (Sesuai Struktur di UTS) */
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    event_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES events(id)
);

/* Data awal untuk pengujian */
INSERT INTO events (title, date, location, quota) 
VALUES 
('Workshop Python', '2025-11-20', 'Aula JTI', 50),
('Seminar AI', '2025-11-22', 'Gedung G', 100);
# Proyek UTS: Campus Event Registration Platform

[cite_start]Proyek ini adalah implementasi sistem registrasi *event* kampus untuk memenuhi UTS Mata Kuliah Interoperabilitas[cite: 3, 4]. [cite_start]Sistem ini menunjukkan interoperabilitas antara *backend* REST API (FastAPI), *database* (SQLite), dan *frontend* HTML sederhana[cite: 6].

## 🛠️ Teknologi yang Digunakan
* **Backend**: FastAPI (Python)
* **Database**: SQLite
* **Frontend**: HTML + Fetch API (JavaScript)
* [cite_start]**Dokumentasi**: Swagger UI (Tugas Bonus 6) [cite: 8]

---

## 📁 Struktur Folder

Proyek ini dipisah menjadi dua komponen utama:
Tentu. Ini adalah *file* `README.md` lengkap yang baru, yang disesuaikan dengan **struktur folder `backend/frontend`** dan **versi sederhana (non-autentikasi)** yang kita sepakati.

*File* ini juga sudah menyertakan bagian *screenshot* yang Anda minta, yang telah disesuaikan dengan nama *file* dari `image_265b40.png`.

Silakan salin dan tempel (copy-paste) seluruh teks di bawah ini ke dalam *file* `README.md` Anda (yang ada di *folder* utama `Interoprobilitas/`).

-----

```markdown
# Proyek UTS: Campus Event Registration Platform

[cite_start]Proyek ini adalah implementasi sistem registrasi *event* kampus untuk memenuhi UTS Mata Kuliah Interoperabilitas[cite: 3, 4]. [cite_start]Sistem ini menunjukkan interoperabilitas antara *backend* REST API (FastAPI), *database* (SQLite), dan *frontend* HTML sederhana[cite: 6].

## 🛠️ Teknologi yang Digunakan
* **Backend**: FastAPI (Python)
* **Database**: SQLite
* **Frontend**: HTML + Fetch API (JavaScript)
* [cite_start]**Dokumentasi**: Swagger UI (Tugas Bonus 6) [cite: 8]

---

## 📁 Struktur Folder

Proyek ini dipisah menjadi dua komponen utama:
```

/Interoprobilitas
├── backend/        (Semua kode FastAPI & database)
│   ├── venv/
│   ├── database.py
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── campus\_events.db  \<-- (Dibuat otomatis)
│
├── frontend/       (File HTML & JavaScript)
│   └── index.html
│
├── Screenshot/     (Berisi screenshot pengujian)
│   ├── GET\_Event.png
│   ├── POST\_Event.png
│   └── ... (dan file .png lainnya)
│
├── create\_db.sql   (Script setup database)
└── README.md

````

---

## 🚀 Cara Menjalankan

Ikuti langkah-langkah ini dari terminal Anda untuk menjalankan proyek dari awal.

### 1. Setup Awal (Hanya sekali)
1.  Buka terminal dan `cd` ke *folder* utama proyek Anda:
    ```bash
    cd C:\Users\narendraryaaa\Documents\Interoprobilitas
    ```
2.  Buat *Virtual Environment (venv)* di dalam *folder* `backend`:
    ```bash
    python -m venv backend\venv
    ```
3.  Aktifkan `venv` tersebut:
    ```bash
    .\backend\venv\Scripts\activate
    ```
4.  Pindah ke *folder* `backend`:
    ```bash
    cd backend
    ```
5.  Install semua *library* yang diperlukan (dari `requirements.txt` versi sederhana):
    ```bash
    pip install -r requirements.txt
    ```

### 2. Membuat Database Baru (Non-Autentikasi)
1.  Pastikan Anda berada di dalam *folder* `backend/` (dengan `(venv)` aktif).
2.  Jalankan perintah ini untuk menghapus *database* lama (jika ada):
    ```bash
    del campus_events.db
    ```
3.  Jalankan perintah ini untuk membuat `campus_events.db` baru menggunakan *script* `.sql` (yang ada di *folder* luar `../`):
    ```bash
    sqlite3 campus_events.db < ..\create_db.sql
    ```
    *(Database Anda sekarang bersih dan siap tanpa data autentikasi).*

### 3. Menjalankan Server Backend
1.  Pastikan Anda masih di dalam *folder* `backend/`.
2.  Jalankan server `uvicorn`:
    ```bash
    uvicorn main:app --reload --reload-exclude "campus_events.db"
    ```
3.  Server akan berjalan di `http://127.0.0.1:8000`.

### 4. Menjalankan Frontend
1.  Buka *File Explorer* Anda.
2.  Pergi ke *folder* `frontend/`.
3.  **Klik dua kali *file* `index.html`** untuk membukanya di *browser* Anda.

---

## 🗺️ Daftar Endpoint API

Semua *endpoint* dapat diuji melalui dokumentasi interaktif (Swagger UI).

### [cite_start]Dokumentasi (Tugas Bonus 6) [cite: 8]
* **`GET /docs`**: Menampilkan antarmuka Swagger UI.

### [cite_start]Events (Tugas 2) [cite: 8]
* **`GET /events`**: Menampilkan semua *event* yang ada.
* **`POST /events`**: Menambah *event* baru.
* **`PUT /events/{id}`**: Mengubah data *event* berdasarkan ID.
* **`DELETE /events/{id}`**: Menghapus *event* berdasarkan ID.

### [cite_start]Participants (Tugas 3) [cite: 8]
* **`POST /register`**: Mendaftarkan peserta baru ke sebuah *event*.
* **`GET /participants`**: Menampilkan semua peserta yang terdaftar.

---

## 🚀 Screenshot Hasil Uji Coba
*(Berikut adalah screenshot pengujian dari `backend/` dan `frontend/`)*

### Uji Coba CRUD Event (dari Swagger UI)
[Detail Event (Hasil GET /events)](Screenshot/GET_Event.png)
[Create Event (POST /events TryOut)](Screenshot/POST_Event_TryOut.png)
[Create Event Sukses (Hasil POST /events)](Screenshot/POST_Event.png)
[Mengubah data Event (PUT /events TryOut)](Screenshot/PUT_Event_TryOut.png)
[Berhasil mengubah data event (Hasil PUT /events)](Screenshot/PUT_Event.png)
[Menghapus Event (DELETE /events TryOut)](Screenshot/DELETE_Event_TryOut.png)
[Berhasil menghapus data event (Hasil DELETE /events)](Screenshot/DELETE_Event.png)

### Hasil Uji Coba User (dari `frontend/index.html`)
[User melihat data event (Tampilan GET /events)](Screenshot/GET_Event_Tampilan.png)
[User register dan memilih daftar Event (Tampilan POST /register)](Screenshot/POST_Participant_Tampilan.png)
[User berhasil register (Hasil POST /register)](Screenshot/POST_Participant.png)

### Hasil uji coba participants (dari Swagger UI)
[Tampilan data participant event (Tampilan GET /participants)](Screenshot/GET_Participant_Tampilan.png)
[Uji Coba GET /participants](Screenshot/GET_Participant_TryOut.png)
[Melihat data participant sukses (Hasil GET /participants)](Screenshot/GET_Participant.png)
````
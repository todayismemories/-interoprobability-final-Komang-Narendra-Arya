# [Campus-Event]

(Tambahkan deskripsi singkat tentang proyek Anda di sini. Jelaskan apa yang dilakukan proyek ini.)

## Cara Menjalankan Proyek

Berikut adalah langkah-langkah untuk menginstal dan menjalankan proyek ini di lingkungan lokal Anda.

### 1. Persiapan Awal

1.  **Clone Repositori**
    ```bash
    git clone [URL_GITHUB_ANDA]
    cd [NAMA_FOLDER_PROYEK]
    ```

2.  **Siapkan Virtual Environment (Venv)**
    * Pindah ke direktori `backend`:
        ```bash
        cd backend
        ```
    * Buat *virtual environment* baru:
        ```bash
        # Windows
        python -m venv venv

        # macOS/Linux
        python3 -m venv venv
        ```
    * Aktifkan *virtual environment*:
        ```bash
        # Windows
        .\venv\Scripts\activate

        # macOS/Linux
        source venv/bin/activate
        ```

3.  **Install Dependensi**
    * Pastikan *virtual environment* Anda sudah aktif (terlihat `(venv)` di awal terminal).
    * Install semua *library* yang dibutuhkan:
        ```bash
        pip install -r requirements.txt
        ```

### 2. Pengaturan Database

1.  **Buat Database Baru**
    * Buka *client* MySQL Anda (misalnya: terminal, DBeaver, atau phpMyAdmin).
    * Buat database baru dengan nama `campus_events_db`.
        ```sql
        CREATE DATABASE campus_events_db;
        ```

2.  **Impor Skema/Data**
    * Impor file `.sql` (yang Anda sebut sebagai `surijet.sql`) ke dalam database `campus_events_db` yang baru saja Anda buat.
    * *Catatan: Anda mungkin perlu menyesuaikan file koneksi database di dalam kode backend Anda (misalnya di `main.py` atau file `config.py`) agar sesuai dengan username dan password MySQL Anda.*

### 3. Menjalankan Server

1.  **Jalankan Server Backend**
    * Pastikan Anda masih berada di dalam folder `backend` dan *virtual environment* Anda aktif.
    * Jalankan server Uvicorn:
        ```bash
        uvicorn main:app --reload
        ```
    * Server sekarang akan berjalan di `http://127.0.0.1:8000`.

2.  **Jalankan Frontend**
    * Buka folder `frontend` di file explorer Anda.
    * Klik dua kali pada file `index.html` untuk membukanya di browser.

---

## Daftar Endpoint API

Dokumentasi API interaktif (Swagger UI) dapat diakses melalui:
`http://127.0.0.1:8000/docs`

### Events
* `GET /events` - [Tugas: 1] [Riset: 0] - Menampilkan semua 'event' yang ada.
* `POST /events` - [Tugas: 2] [Riset: 0] - Mendaftarkan 'event' baru.
* `GET /events/{id}` - [Tugas: 3] [Riset: 0] - Menampilkan 'event' berdasarkan ID.
* `PUT /events/{id}` - [Tugas: 4] [Riset: 0] - Mengubah data 'event' berdasarkan ID.
* `DELETE /events/{id}` - [Tugas: 5] [Riset: 0] - Menghapus 'event' berdasarkan ID.

### Participants
* `GET /participants` - [Tugas: 5] [Riset: 0] - Menampilkan semua peserta yang terdaftar.
* `POST /participants` - [Tugas: 6] [Riset: 0] - Mendaftarkan peserta baru (via 'event').

---

## Fungsionalitas & Alur Pengguna

### 1. Fungsionalitas Event (CRUD)
Admin dapat melakukan fungsionalitas CRUD (Create, Read, Update, Delete) pada data 'event'.

* [Lihat Tampilan Event](Screenshot/GET_Event_Tampilan.png)
* [Hapus Event](Screenshot/DELETE_Event_Tampilan.png)
* [Melihat Form Event (Uji Coba)](Screenshot/POST_Event_TryOut.png)
* [Melihat Event (Full)](Screenshot/GET_Event.png)
* [Memperbarui Event (Uji Coba)](Screenshot/PUT_Event_TryOut.png)
* [Tampilan Awal](Screenshot/GET_Event_Tampilan.png)

### 2. Alur Pengguna (Frontend & Pendaftaran)
Pengguna umum dapat melihat daftar 'event' dan mendaftarkan diri melalui 'frontend' (`index.html`).

* [Lihat Tampilan Frontend](Screenshot/GET_Event_Tampilan.png)
* [Melihat Event (Frontend)](Screenshot/GET_Event_Tampilan.png)
* [Uji Coba Pendaftaran Peserta](Screenshot/POST_Participant_TryOut.png)
* [Tampilan Peserta Terdaftar](Screenshot/GET_Participant_Tampilan.png)

### 3. Melihat Peserta (Feedback Panitia)
Panitia dapat melihat daftar lengkap semua peserta yang telah terdaftar.

* [Lihat Tampilan Request Data](Screenshot/GET_Participant_Tampilan.png)
* [Melihat Semua Peserta (Uji Coba)](Screenshot/GET_Participant_TryOut.png)

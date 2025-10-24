## 📸 Screenshot Hasil Uji Coba

Berikut adalah dokumentasi visual dari alur pengujian API menggunakan Swagger UI dan *frontend*.

---
### 1. Manajemen Event (Endpoint Publik)

Siapa pun dapat melakukan operasi CRUD (Create, Read, Update, Delete) pada data *event*.

| Aksi | Tampilan Request (Uji Coba) | Hasil Sukses |
| :--- | :---: | :---: |
| **Melihat Semua Event (GET)** | ![Uji Coba Melihat Event](Screenshot/GET_Event_TryOut.png) | ![Hasil Melihat Event](Screenshot/GET_Event.png) |
| **Membuat Event Baru (POST)** | ![Uji Coba Membuat Event](Screenshot/POST_Event_TryOut.png) | ![Hasil Membuat Event](Screenshot/POST_Event.png) |
| **Memperbarui Event (PUT)** | ![Uji Coba Memperbarui Event](Screenshot/PUT_Event_TryOut.png) | ![Hasil Memperbarui Event](Screenshot/PUT_Event.png) |
| **Menghapus Event (DELETE)**| ![Uji Coba Menghapus Event](Screenshot/DELETE_Event_TryOut.png) | ![Hasil Menghapus Event](Screenshot/DELETE_Event.png) |

---
### 2. Alur Pengguna (Frontend & Pendaftaran)

Pengguna umum dapat melihat daftar *event* dan mendaftarkan diri melalui *frontend* (`index.html`) atau API.

| Aksi | Tampilan Frontend | Hasil Sukses (dari API) |
| :--- | :---: | :---: |
| **Melihat Event (Frontend)** | ![Melihat Event di Frontend](Screenshot/GET_Event_Tampilan.png) | (Tampilan di atas) |
| **Mendaftar (Frontend)** | ![Form Pendaftaran](Screenshot/POST_Participant_Tampilan.png) | ![Berhasil Mendaftar](Screenshot/POST_Participant.png) |

---
### 3. Melihat Peserta (Endpoint Publik)

Siapa pun dapat melihat daftar lengkap semua peserta yang telah terdaftar.

| Aksi | Tampilan Request (Uji Coba) | Hasil Sukses |
| :--- | :---: | :---: |
| **Melihat Semua Peserta (GET)** | ![Uji Coba Melihat Peserta](Screenshot/GET_Participant_TryOut.png) | ![Hasil Melihat Peserta](Screenshot/GET_Participant.png) |

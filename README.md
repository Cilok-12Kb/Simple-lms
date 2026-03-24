# 👨‍💻 Author

Nama: Mahammad Ibadullah  
NIM: A11.2023.15275  

Project ini dibuat untuk keperluan pembelajaran Docker + Django.

---

# 📚 Simple LMS - Django + PostgreSQL + Docker

Project ini adalah setup dasar **Learning Management System (LMS)** menggunakan **Django**, **PostgreSQL**, dan **Docker**. Project ini dirancang untuk memudahkan development environment tanpa perlu install dependency secara manual di local machine.

---

# 🚀 Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone <repo-url>
cd simple-lms
```

---

### 2. Jalankan Docker

```bash
docker compose up --build
```

---

### 3. Akses Aplikasi

Buka browser:

```
http://localhost:8000
```

Jika berhasil, akan muncul halaman default Django 🚀

---

# ⚙️ Environment Variables

Konfigurasi environment terdapat pada file `.env`.

Contoh:

```env
DEBUG=True
SECRET_KEY=django-insecure-key

DB_NAME=lms_db
DB_USER=lms_user
DB_PASSWORD=lms_password
DB_HOST=db
DB_PORT=5432
```

### Penjelasan:

| Variable    | Deskripsi                    |
| ----------- | ---------------------------- |
| DEBUG       | Mode debug Django            |
| SECRET_KEY  | Secret key Django            |
| DB_NAME     | Nama database PostgreSQL     |
| DB_USER     | Username PostgreSQL          |
| DB_PASSWORD | Password PostgreSQL          |
| DB_HOST     | Host database (gunakan `db`) |
| DB_PORT     | Port PostgreSQL              |

---

# 🐳 Services yang Digunakan

Project ini menggunakan Docker Compose dengan 2 service utama:

### 1. Web (Django)

* Menjalankan aplikasi Django
* Port: `8000`

### 2. Database (PostgreSQL)

* Database utama
* Port: `5432`
* Data disimpan di volume Docker

---

# 🧱 Struktur Project

```
simple-lms/
├── docker-compose.yml
├── Dockerfile
├── .env
├── .env.example
├── requirements.txt
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

---

# 🗄️ Perintah Penting

### Migrasi Database

```bash
docker compose exec web python manage.py migrate
```

---

### Membuat Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

### Masuk ke Container

```bash
docker compose exec web bash
```

---

### Melihat Container Aktif

```bash
docker ps
```

---

### Melihat Log

```bash
docker logs lms_web
```

---

### Stop Project

```bash
docker compose down
```

---

# 📂 Static Files

Konfigurasi static files di `settings.py`:

```python
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

# ⚠️ Troubleshooting

### ❌ Tidak bisa konek ke database

✔ Pastikan:

```env
DB_HOST=db
```

**Jangan gunakan `localhost`**

---

### ❌ Port sudah digunakan

```bash
docker compose down
```

Atau ganti port di `docker-compose.yml`

---

### ❌ Container error / tidak jalan

Cek:

```bash
docker ps
docker logs lms_web
```

---

### ❌ Perubahan tidak muncul

Coba rebuild:

```bash
docker compose up --build
```

---

# 📸 Screenshot (WAJIB)

Tambahkan screenshot berikut:

1. Halaman Django (`localhost:8000`)
2. Container berjalan (`docker ps`)

Contoh:

```
docs/
├── home.png
├── docker.png
```

---

# 📤 Cara Upload ke GitHub

```bash
git init
git add .
git commit -m "Initial commit simple LMS"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

---

# ✅ Checklist

* [ ] Docker berhasil dijalankan
* [ ] Django tampil di browser
* [ ] Database PostgreSQL terhubung
* [ ] Migrasi berhasil tanpa error
* [ ] Struktur project sesuai
* [ ] README lengkap
* [ ] Screenshot tersedia

---

# 🎯 Catatan Penting

* Gunakan `.env` untuk konfigurasi
* Jangan hardcode credential database
* Gunakan `db` sebagai host database
* Selalu stop container jika terjadi error

---

# 📌 Next Step (Pengembangan LMS)

Setelah setup berhasil, kamu bisa lanjut:

* Membuat app `courses`
* Sistem user & authentication
* Enrollment siswa
* Upload materi
* Quiz / assignment

---

## 📸 Screenshot

### Tampilan awal Django
![Tampilan awal Django](images/image1.png)

### Succes Setup and Instalasi
![Succes Setup and Instalasi](images/image3.png)

### migration and creat super user
![migration and creat super user](images/image2.png)

---

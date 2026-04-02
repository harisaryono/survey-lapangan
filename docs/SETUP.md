# Setup Awal

## Backend
1. Masuk ke folder `backend`
2. Buat virtual environment
3. Install dependency dari `requirements.txt`
4. Salin `.env.example` menjadi `.env`
5. Jalankan API dengan Uvicorn

Contoh:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Frontend
1. Masuk ke folder `frontend`
2. Install dependency
3. Jalankan server development

Contoh:

```bash
cd frontend
npm install
npm run dev
```

## Database
Gunakan `docker-compose.yml` di root proyek untuk menjalankan PostgreSQL lokal.

```bash
docker compose up -d
```

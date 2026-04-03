# Cara Menjalankan Versi V3

## 1. Jalankan PostgreSQL
Dari root project:

```bash
docker compose up -d
```

## 2. Jalankan backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.scripts.init_db
python -m app.scripts.seed_users_v2
uvicorn app.main_v3:app --reload
```

Backend akan aktif di:
- http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## 3. Jalankan frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend akan aktif di:
- http://127.0.0.1:3000

## 4. Akun awal
- admin / admin123
- ketua / ketua123

## 5. Endpoint inti yang sudah siap dicoba
- `POST /api/v1/auth/login`
- `GET /api/v1/surveys`
- `POST /api/v1/surveys`
- `GET /api/v1/surveys/{survey_id}`
- `POST /api/v1/forms/{form_id}/claim`
- `POST /api/v1/forms/{form_id}/submit`
- `POST /api/v1/forms/{form_id}/approve`
- `POST /api/v1/forms/{form_id}/revision`
- `POST /api/v1/forms/{form_id}/unlock`
- `GET /api/v1/findings/forms/{form_id}`
- `PUT /api/v1/findings/forms/{form_id}`

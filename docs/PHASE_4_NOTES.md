# Phase 4 Notes

## Yang ditambahkan
- `backend/app/core/security.py`
- `backend/app/schemas/auth.py`
- `backend/app/services/auth_service.py`
- `backend/app/services/form_workflow_service.py`
- `backend/app/schemas/workflow.py`
- `backend/app/api/v1/auth_v2.py`
- `backend/app/api/v1/forms_v2.py`
- `backend/app/api/router_v2.py`

## Fungsi utama
- login JWT dasar
- claim form
- submit form
- approve form
- request revision
- unlock form

## Cara pakai sementara
Karena file router lama belum ditimpa di sesi ini, gunakan `router_v2.py` sebagai acuan integrasi. Saat bekerja lokal, ubah import di `main.py` dari:

```python
from app.api.router import api_router
```

menjadi:

```python
from app.api.router_v2 import api_router_v2 as api_router
```

atau langsung sesuaikan pemanggilan `include_router` di `main.py`.

## Catatan password seed
Script `seed_users.py` masih membuat user dengan `password_hash="change-me"`. Agar login JWT bekerja, Anda perlu mengganti seed tersebut dengan hash bcrypt nyata atau menjalankan penyesuaian lokal saat pengembangan.

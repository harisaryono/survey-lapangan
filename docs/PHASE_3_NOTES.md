# Phase 3 Notes

## Yang sudah ditambahkan
- model database inti untuk user, survey, survey member, survey form, dan form finding
- service `create_survey` yang otomatis membuat form default
- service `claim_form` untuk mekanisme lock awal
- endpoint workflow draft terpisah pada:
  - `backend/app/api/v1/surveys_workflow.py`
  - `backend/app/api/v1/forms_workflow.py`
- seed user awal
- kerangka Alembic
- skeleton halaman dashboard dan detail survei di frontend

## Kenapa endpoint workflow dibuat terpisah
File router utama yang lebih lama di branch ini sudah terlanjur dibuat dalam bentuk placeholder. Tool GitHub yang tersedia di sesi ini lebih andal untuk menambah file baru dibanding menimpa file lama. Karena itu, endpoint workflow fase 3 dibuat terpisah agar logika bisnis tetap dapat dipersiapkan tanpa merusak scaffold yang sudah ada.

## Langkah penyambungan berikutnya
1. import router workflow baru ke `backend/app/api/router.py`
2. ganti placeholder lama setelah bekerja di editor lokal
3. buat migration awal Alembic
4. tambah JWT auth nyata
5. sambungkan frontend ke API

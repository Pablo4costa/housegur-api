housegur-api/
├─ app/
│   ├─ __init__.py
│   ├─ main.py
│   ├─ database.py
│   ├─ crud.py
│   ├─ schemas.py
│   └─ routers/
│       ├─ __init__.py
│       ├─ auth.py
│       ├─ properties.py
│       └─ transactions.py
├─ .env
├─ requirements.txt
└─ README.md


--Start command en railway:
--   uvicorn app.main:app --host 0.0.0.0 --port $PORT

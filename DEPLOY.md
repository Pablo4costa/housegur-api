# Deploy notes for housegur-api

Quick checklist to deploy to Railway (or similar PaaS).

1. Environment
   - Ensure the environment variable `DATABASE_URL` is set in the Railway project settings. Example (do NOT commit credentials):
     - `mysql+pymysql://user:password@host:3306/housegur`
   - This repository's `app/database.py` will rewrite a URL that starts with `mysql://` to `mysql+pymysql://` automatically, so both forms work.

2. Start command
   - Railway should use the start command in the `Procfile`:
     ```text
     web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
     ```

3. Python version
   - If you need to pin Python, configure the Railway project runtime (or add a runtime file). If you hit dependency errors on very new Python versions, try Python 3.11.

4. Database
   - The code depends on the `housegur` schema and stored procedures (`sp_comprar_tokens`, `sp_vender_tokens`). Make sure the DB pointed by `DATABASE_URL` has the schema and SPs installed.

5. Secrets & safety
   - Never commit `.env` with credentials. Use Railway environment variables.
   - If you pasted a real password in a public repo by mistake, rotate it.

6. Troubleshooting
   - Import errors referencing `app.routers`: ensure `app` is a Python package (this repo includes `app/__init__.py` and `app/routers/__init__.py`).
   - `ModuleNotFoundError: No module named 'MySQLdb'`: install `mysqlclient` or prefer `pymysql`. This repo uses `pymysql` and the DB helper rewrites `mysql://` → `mysql+pymysql://`.

7. Quick local test
   ```bash
   pip install -r requirements.txt
   export DATABASE_URL='mysql+pymysql://user:pass@host:port/housegur'
   uvicorn app.main:app --reload
   # open http://127.0.0.1:8000/
   ```

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Read DATABASE_URL from env. If the URL uses the legacy `mysql://` scheme,
# SQLAlchemy will try to import `MySQLdb` (mysqlclient). This project lists
# `pymysql` in requirements, so prefer the `mysql+pymysql://` driver when
# appropriate to avoid ModuleNotFoundError: No module named 'MySQLdb'.
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("mysql://"):
	DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

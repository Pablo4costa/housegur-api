from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Read DATABASE_URL from environment.
# If it uses the legacy `mysql://` scheme, rewrite to `mysql+pymysql://`
# because this project lists `pymysql` in requirements, not `mysqlclient`.
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable is not set. "
        "Please configure it in your environment or .env file. "
        "Example: mysql+pymysql://user:password@host:3306/housegur"
    )

# Rewrite mysql:// to mysql+pymysql:// to use pymysql driver
if DATABASE_URL.startswith("mysql://"):
    DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

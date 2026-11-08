"""
AyuMitra Database Session

Provides SQLAlchemy session management.
"""

from sqlalchemy.orm import sessionmaker

from src.database.connection import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_db():
    """
    FastAPI dependency for database sessions.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
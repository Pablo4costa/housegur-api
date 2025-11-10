"""Routers package initializer.

Expose router modules for easier imports: `from app.routers import auth, properties, transactions`.
"""

from . import auth  # noqa: F401
from . import properties  # noqa: F401
from . import transactions  # noqa: F401

__all__ = ["auth", "properties", "transactions"]

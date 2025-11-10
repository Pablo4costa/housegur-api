"""App package initializer.

This file makes `app` an explicit package so imports like
`from app.routers import ...` work reliably in deployment.
"""

__all__ = ["main", "crud", "database", "schemas", "routers"]

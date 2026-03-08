# FastAPI:
#
# 1.1.
# 1.2. pip install "fastapi[standard]"
# 2. mysite: admin, api, database/ __init__.py
# 3. main.py: shop_app
# 4. database: db.py (SQLAlchemy)
# 5. config.py (SECRET_KEY)
# 6. database: models.py (Mapped, mapped_column)
# 7. pip install Alembic
# 7.1. alembic init migrations
# 7.2. alembic revision --autogenerate
# 7.3. alembic upgrade head
# 8. database: schema.py (Pydantic, JSON, Валидация)
# 9. api: CRUD (APIRouter, HTTPException, Depends, Session)
# 10. uvicorn main:shop_app, uvicorn main:shop_app --reload, main.py if name
# 11. auth.py: JWT (register, login, logout, refresh, ХЭШ)pip install fastapi




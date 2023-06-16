from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), index=True, nullable=False)
    password_hash = Column(String(512), index=True, nullable=False)
    description = Column(String(512), nullable=True)
    avatar_img = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_public = Column(Boolean, default=True, nullable=False)

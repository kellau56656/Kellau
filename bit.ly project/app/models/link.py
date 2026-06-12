from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    original_url = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
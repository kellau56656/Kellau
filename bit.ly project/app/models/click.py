from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Click(Base):
    __tablename__ = "clicks"

    id = Column(Integer, primary_key=True)

    ip = Column(String)
    user_agent = Column(String)

    link_id = Column(Integer, ForeignKey("links.id"))
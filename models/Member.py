from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    loans = relationship("Loan", back_populates="member")  # <-- Add this line


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define the relationship to Book
    books = relationship("Book", back_populates="author")  # <-- Add this line

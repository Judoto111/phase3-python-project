from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define the relationship to Book
    books = relationship("Book", back_populates="genre")  # <-- Add this line


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    # Define relationships
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    loans = relationship("Loan", back_populates="book")  # <-- Add this line

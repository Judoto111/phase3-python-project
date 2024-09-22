from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    loan_date = Column(Date)
    return_date = Column(Date)

    book = relationship("Book", back_populates="loans")  # <-- Add this line
    member = relationship("Member", back_populates="loans")

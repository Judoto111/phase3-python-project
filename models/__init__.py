from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .Author import Author
from .Book import Book
from .Genre import Genre
from .Member import Member
from .Loan import Loan

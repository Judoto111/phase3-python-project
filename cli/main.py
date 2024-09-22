import click
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Author, Book, Genre, Member, Loan

DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Library Management CLI."""
    pass

@cli.command()
def init_db():
    """Create the database tables."""
    Base.metadata.create_all(engine)
    click.echo("Initialized the database.")

@cli.command()
@click.argument('name')
def add_author(name):
    """Add a new author."""
    session = Session()
    author = Author(name=name)
    session.add(author)
    session.commit()
    click.echo(f'Added author: {name}')
    session.close()

@cli.command()
@click.argument('title')
@click.argument('author_name')
@click.argument('genre_name')
def add_book(title, author_name, genre_name):
    """Add a new book with author and genre."""
    session = Session()
    
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
    
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)

    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    click.echo(f'Added book: {title} by {author_name} in {genre_name}')
    session.close()

@cli.command()
def list_books():
    """List all books."""
    session = Session()
    books = session.query(Book).all()
    if not books:
        click.echo("No books found.")
    else:
        for book in books:
            click.echo(f'Title: {book.title}, Author: {book.author.name}, Genre: {book.genre.name}')
    session.close()

@cli.command()
def list_authors():
    """List all authors."""
    session = Session()
    authors = session.query(Author).all()
    if not authors:
        click.echo("No authors found.")
    else:
        click.echo("Authors:")
        for author in authors:
            click.echo(f'{author.id}: {author.name} - {author.bio}')
    session.close()

@cli.command()
@click.argument('name')
@click.argument('email')
def add_member(name, email):
    """Add a new member."""
    session = Session()
    member = Member(name=name, email=email)
    session.add(member)
    session.commit()
    click.echo(f'Added member: {name}')
    session.close()

@cli.command()
@click.argument('book_id', type=int)
@click.argument('member_id', type=int)
@click.argument('loan_date_str')
@click.argument('return_date_str')
def add_loan(book_id, member_id, loan_date_str, return_date_str):
    """Add a loan for a book to a member."""
    session = Session()
    
    try:
        loan_date = datetime.datetime.strptime(loan_date_str, "%Y-%m-%d").date()
        return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()

        loan = Loan(book_id=book_id, member_id=member_id, loan_date=loan_date, return_date=return_date)
        session.add(loan)
        session.commit()
        click.echo(f'Added loan for book ID {book_id} to member ID {member_id}.')
    except ValueError as e:
        click.echo(f"Error parsing dates: {e}")
    except Exception as e:
        click.echo(f"Error adding loan: {e}")
    finally:
        session.close()

@cli.command()
@click.argument('book_title')
@click.argument('member_id')
def loan_book(book_title, member_id):
    """Loan a book to a member."""
    session = Session()
    book = session.query(Book).filter_by(title=book_title).first()
    member = session.query(Member).get(member_id)

    if book and member:
        loan_date = datetime.date.today()  # Set to today or another logic for loan date
        return_date = loan_date + datetime.timedelta(days=14)  # Example: 2 weeks loan period
        
        loan = Loan(book_id=book.id, member_id=member.id, loan_date=loan_date, return_date=return_date)
        session.add(loan)
        session.commit()
        click.echo(f'Loaned "{book_title}" to member ID {member_id}.')
    else:
        click.echo("Book or member not found.")
    session.close()

@cli.command()
def test():
    """Test command."""
    click.echo("Test command executed.")

if __name__ == "__main__":
    cli()

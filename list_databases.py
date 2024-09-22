from sqlalchemy import create_engine, inspect, text


DATABASE_URL = "mysql+pymysql://root:Judoto!2024@localhost/library"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        
        authors_query = text("SELECT * FROM authors")
        authors_result = connection.execute(authors_query).fetchall()
        
        print("Authors:")
        for author in authors_result:
            print(author)

        
        books_query = text("SELECT * FROM books")
        books_result = connection.execute(books_query).fetchall()
        
        print("\nBooks:")
        for book in books_result:
            print(book)

except Exception as e:
    print("An error occurred while connecting to the database:")
    print(e)

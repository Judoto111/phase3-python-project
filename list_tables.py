from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import OperationalError


db_url = "mysql+pymysql://root:Judoto!@2024@localhost/your_database"

try:
    
    engine = create_engine(db_url)
    inspector = inspect(engine)

    
    tables = inspector.get_table_names()

    if tables:
        print("Tables in the database:")
        for table in tables:
            print(table)
    else:
        print("No tables found in the database.")
except OperationalError as e:
    print(f"An error occurred while connecting to the database: {e}")

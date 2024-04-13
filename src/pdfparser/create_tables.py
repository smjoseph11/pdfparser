from pdfparser.model import SQLModel, create_engine

from pdfparser import config
from pdfparser.orm import Base

# Define the database connection URL

# Create a database engine
engine = create_engine(config.get_postgres_uri())

# Create all tables
SQLModel.metadata.create_all(engine)

print("Tables created successfully!")

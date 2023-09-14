from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}" \
                          f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# while True:
#     try:
#         connection = psycopg2.connect(user="postgres",
#                                       password="postgres",
#                                       host="localhost",
#                                       port="5432",
#                                       database="fastapi",
#                                       cursor_factory=RealDictCursor)  # not standard way of storing connection details
#         cursor = connection.cursor()
#         print("Database connection was successful")
#         break
#     except (Exception, psycopg2.Error) as error:
#         print("Error while connecting to PostgreSQL - Error is", error)
#         time.sleep(2)

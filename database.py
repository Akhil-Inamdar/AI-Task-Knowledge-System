# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from app.models.user import User
# from app.models.task import Task
# from app.models.document import Document

# Base.metadata.create_all(bind=engine)

# DATABASE_URL = "mysql+pymysql://root:Akhil%40123@localhost/ai_task_system"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# from app.models.user import User

# Base.metadata.create_all(bind=engine)

# from app.models.task import Task


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Akhil%40123@localhost/ai_task_system"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Import models ONLY AFTER Base is created
from app.models.user import User
from app.models.task import Task
from app.models.document import Document

Base.metadata.create_all(bind=engine)

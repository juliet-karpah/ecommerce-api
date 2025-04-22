from sqlmodel import create_engine

database_name = ""
database_url = f""

engine = create_engine(database_url, echo=True)
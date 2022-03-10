from flask import current_app, g


class Database:

    @classmethod
    def get_db(cls):
        if not g.get('session', None):
            from dotenv import load_dotenv
            from os import getenv
            from sqlalchemy import create_engine
            from sqlalchemy.ext.declarative import declarative_base
            from sqlalchemy.orm import sessionmaker

            # load .env file environment variables
            load_dotenv()

            # get SQL Server connection string from .env
            mysql_connection_string = getenv("MYSQL_CONNECTION_STRING")
            # create sqlalchemy engine
            engine = create_engine(mysql_connection_string)
            # declare Base
            g.Base = declarative_base()
            g.Base.metadata.create_all(engine)
            # create a DB Session
            Session = sessionmaker()
            Session.configure(bind=engine)
            g.session = Session()

        return g.session

    @classmethod
    def close_db(cls, e=None):
        db = g.get("session", None)
        if db is not None:
            db.close()

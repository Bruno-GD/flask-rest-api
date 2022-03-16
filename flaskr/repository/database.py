from flask import g
from .types.Item import Item
from sqlalchemy.orm.session import Session  # just for annotations
import click


class Database:

    @staticmethod
    def get_session() -> Session:
        from dotenv import load_dotenv
        from os import getenv
        from sqlalchemy import create_engine
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker

        # load .env file environment variables
        if getenv("MYSQL_CONNECTION_STRING", None) is None:
            load_dotenv()

        # get SQL Server connection string from .env
        mysql_connection_string = getenv("MYSQL_CONNECTION_STRING")
        # create sqlalchemy engine
        engine = create_engine(mysql_connection_string)
        # declare Base
        Base = declarative_base()
        Base.metadata.create_all(engine)
        # create a DB Session
        Session = sessionmaker()
        Session.configure(bind=engine)
        return Session()

    @classmethod
    def get_db(cls):
        if not g.get('session', None):
            g.session = cls.get_session()

        return g.session

    @classmethod
    def close_db(cls, e=None):
        db = cls.get_db()
        if db is not None:
            db.commit()
            db.close()

    @staticmethod
    @click.command()
    def init_db():
        db = Database.get_session()
        db.execute("DROP TABLE IF EXISTS `items`")
        db.execute("""CREATE TABLE IF NOT EXISTS `items` (
                       `id` INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                       `name` VARCHAR(50),
                       `sell_in` INT(3),
                       `quality` INT(3)
                   )""")
        insert_queries = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        ]
        db.add_all(insert_queries)
        db.commit()

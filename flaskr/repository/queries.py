from flaskr.repository.database import Database
from flaskr.repository.types.Item import Item


class Query(Database):

    @classmethod
    def get_all(cls, filter_by: dict[str, any] = {}) -> list[dict[str, any]]:
        """
        Make a query to database, filtering by or not

        :param filter_by: dict containing all "columns" to filter by
        :return: list of dict containing the query result
        """
        db = cls.get_db()
        items: list[Item] = db.query(Item).filter_by(**filter_by).all()
        return [item.serialized for item in items]

    @classmethod
    def get_one(cls, filter_by: dict[str, any] = {}) -> None or dict[str, any]:
        """
        Make a query to database, filtering by or not

        :param filter_by:  dict containing all "columns" to filter by
        :return: dict or None
        """
        db = cls.get_db()
        item = db.query(Item).filter_by(**filter_by).one_or_none()
        return item.serialized if item is not None else None

    @classmethod
    def insert_one(cls, item: dict[str, any]) -> dict[str, any]:
        """
        Make a query to database inserting new item

        :param item: dict containing all "columns" to insert at
        :return: the inserted item as dict
        """
        db = cls.get_db()
        new_item = Item(**item)
        db.add(new_item)
        return new_item.serialized

    @classmethod
    def delete_all(cls, filter_by: dict[str, any]) -> None:
        db = cls.get_db()
        db.query(Item).filter_by(**filter_by).delete()

    @classmethod
    def update_all(cls, filter_by: dict[str, any], new_data: dict[str, any]) -> None:
        db = cls.get_db()
        db.query(Item).filter_by(**filter_by).update(new_data)

from . import Base
from sqlalchemy import Column, String, Integer


class Item(Base):
    __tablename__ = "items"
    name = Column(String(length=50), primary_key=True)
    sell_in = Column(Integer)
    quality = Column(Integer)

    @property
    def serialized(self):
        return {
            "name": self.name,
            "sell_in": self.sell_in,
            "quality": self.quality
        }

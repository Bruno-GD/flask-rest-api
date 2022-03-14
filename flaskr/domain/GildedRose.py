from .types.NormalItem import NormalItem
from .types.ConjuredItem import ConjuredItem
from .types.SulfurasItem import Sulfuras
from .types.BackstageItem import Backstage
from .types.AgedBrieItem import AgedBrie


# enum
class Itemizer:
    ITEM_OBJ = {
        "Sulfuras, Hand of Ragnaros": Sulfuras,
        "Aged Brie": AgedBrie,
        "Backstage passes to a TAFKAL80ETC concert": Backstage,
        "Conjured Mana Cake": ConjuredItem,
        "+5 Dexterity Vest": ConjuredItem,
    }

    @classmethod
    def get(cls, name: str, sell_in: int, quality: int) -> NormalItem:
        if name in cls.ITEM_OBJ:
            return cls.ITEM_OBJ[name](name, sell_in, quality)
        return NormalItem(name, sell_in, quality)


# Code extracted from: https://github.com/dfleta/flask-rest-ci-boilerplate
class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            # qué items hay en este if? => clases
            item.update_quality()

    def get_items(self) -> list:
        return self.items
# end

    @staticmethod
    def get_item_typeof(name: str, sell_in: int, quality: int, **kwargs) -> NormalItem:
        return Itemizer.get(name, sell_in, quality)

    @classmethod
    def get_items_typeof(cls, raw_items: list[dict]) -> list[NormalItem]:
        items = []
        for raw_item in raw_items:
            items.append(cls.get_item_typeof(**raw_item))
        return items

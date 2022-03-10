from .types import \
    NormalItem,\
    AgedBrieItem,\
    BackstageItem,\
    ConjuredItem,\
    SulfurasItem


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

    @staticmethod
    def get_item_typeof(name: str, sell_in: int, quality: int) -> object:
        org_name = name
        name = name.lower()
        if "brie" in name:
            return AgedBrieItem.AgedBrie(org_name, sell_in, quality)
        elif "backstage" in name:
            return BackstageItem.Backstage(org_name, sell_in, quality)
        elif "conjured" in name:
            return ConjuredItem.ConjuredItem(org_name, sell_in, quality)
        elif "sulfuras" in name:
            return SulfurasItem.Sulfuras(org_name, sell_in, quality)
        else:
            return NormalItem.NormalItem(org_name, sell_in, quality)

from .NormalItem import NormalItem
from .Item import Item


# Code extracted from: https://github.com/dfleta/flask-rest-ci-boilerplate
class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # Override metodo setQuality de NormalItem
    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    # Override metodo update_quality de la Interfaz
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()

from .NormalItem import NormalItem
from .Item import Item


# Code extracted from: https://github.com/dfleta/flask-rest-ci-boilerplate
class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # Override metodo update_quality de la interfaz
    def update_quality(self):
        assert self.quality == 80, "quality de %s distinta de 80" % self.__class__.__name__
        pass

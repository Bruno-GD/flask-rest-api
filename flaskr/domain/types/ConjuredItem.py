from .NormalItem import NormalItem


# Code extracted from: https://github.com/dfleta/flask-rest-ci-boilerplate
class ConjuredItem(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override metodo update_quality de la Interfaz
    # Heredado a traves de NormalItem
    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()

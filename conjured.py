from item import Item


class Conjured(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def calc(self):
        self.quality -= 2
        self.sell_in -= 1



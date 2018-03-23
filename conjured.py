from item import Item


class Conjured(Item):
    def __init__(self, item):
        if type(item).__name__ == 'Item':
            super().__init__(item.name, item.sell_in, item.quality)

    def calc(self):
        self.quality -= 2
        self.sell_in -= 1



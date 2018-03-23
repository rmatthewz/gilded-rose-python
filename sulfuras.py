from item import Item


class Sulfuras(Item):
    def __init__(self, item):
        if type(item).__name__ == 'Item':
            super().__init__(item.name, item.sell_in, item.quality)

    def calc(self):
        pass


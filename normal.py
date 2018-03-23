from item import Item


class Normal(Item):
    def __init__(self, item):
        if type(item).__name__ == 'Item':
            super().__init__(item.name, item.sell_in, item.quality)

    def calc(self):
        if self.sell_in == 0:
            self.quality -= 2
        else:
            self.quality -= 1
        self.sell_in -= 1



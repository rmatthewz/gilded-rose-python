from item import Item


class BackstagePass(Item):
    def __init__(self, item):
        if type(item).__name__ == 'Item':
            super().__init__(item.name, item.sell_in, item.quality)

    def calc(self):
        if self.sell_in <= 10:
            self.quality += 1
        if self.sell_in <= 5:
            self.quality += 1
        if self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality += 1
        self.sell_in -= 1


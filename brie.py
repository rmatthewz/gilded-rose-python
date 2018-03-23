from item import Item


class Brie(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def calc(self):
        if self.sell_in <= 10:
            self.quality += 1
        if self.sell_in <= 5:
            self.quality += 1
        if self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality += 1
        if self.quality >= 50:
            self.quality = 50
        self.sell_in -= 1

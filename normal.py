from item import Item


class Normal(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def calc(self):
        if self.sell_in == 0:
            self.quality -= 2
        else:
            self.quality -= 1
        self.sell_in -= 1



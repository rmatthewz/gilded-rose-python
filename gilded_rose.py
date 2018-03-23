class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            if "Aged Brie" == items[i].name:
                items[i] = GildedRose.update_aged_brie(items[i])
                continue

            if "Backstage passes to a TAFKAL80ETC concert" == items[i].name:
                items[i] = GildedRose.update_backstage_pass(items[i])
                continue

            if "Sulfuras, Hand of Ragnaros" == items[i].name:
                items[i] = GildedRose.update_sulfuras(items[i])
                continue

            if "Conjured Mana Cake" == items[i].name:
                items[i] = GildedRose.update_conjured(items[i])
                continue

            items[i] = GildedRose.update_normal(items[i])

    @staticmethod
    def update_normal(item):
        if item.sell_in == 0:
            item.quality -= 2
        else:
            item.quality -= 1
        item.sell_in -= 1

        return item

    @staticmethod
    def update_aged_brie(item):
        if item.sell_in <= 10:
            item.quality += 1

        if item.sell_in <= 5:
            item.quality += 1

        if item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality += 1

        if item.quality >= 50:
            item.quality = 50

        item.sell_in -= 1

        return item

    @staticmethod
    def update_backstage_pass(item):
        if item.sell_in <= 10:
            item.quality += 1

        if item.sell_in <= 5:
            item.quality += 1

        if item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality += 1

        if item.quality >= 50:
            item.quality = 50

        item.sell_in -= 1

        return item

    @staticmethod
    def update_sulfuras(item):

        return item

    @staticmethod
    def update_conjured(item):
        if item.sell_in == 0:
            item.quality -= 1

        item.quality -= 1
        item.sell_in -= 1

        return item

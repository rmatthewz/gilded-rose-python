from brie import Brie
from backstage_pass import BackstagePass
from sulfuras import Sulfuras
from normal import Normal
from conjured import Conjured


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
        normal = Normal(item.name, item.sell_in, item.quality)
        normal.calc()
        return normal

    @staticmethod
    def update_aged_brie(item):
        brie = Brie(item.name, item.sell_in, item.quality)
        brie.calc()
        return brie

    @staticmethod
    def update_backstage_pass(item):
        backstage_pass = BackstagePass(item.name, item.sell_in, item.quality)
        backstage_pass.calc()
        return backstage_pass

    @staticmethod
    def update_sulfuras(item):
        sulfuras = Sulfuras(item.name, item.sell_in, item.quality)
        sulfuras.calc()
        return sulfuras

    @staticmethod
    def update_conjured(item):
        conjured = Conjured(item.name, item.sell_in, item.quality)
        conjured.calc()
        return conjured

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
                temp_item = Brie(items[i])
            elif "Backstage passes to a TAFKAL80ETC concert" == items[i].name:
                temp_item = BackstagePass(items[i])
            elif "Sulfuras, Hand of Ragnaros" == items[i].name:
                temp_item = Sulfuras(items[i])
            elif "Conjured Mana Cake" == items[i].name:
                temp_item = Conjured(items[i])
            else:
                temp_item = Normal(items[i])
            temp_item.calc()
            items[i] = temp_item

from brie import Brie
from backstage_pass import BackstagePass
from normal import Normal
from conjured import Conjured


class GildedRose:
    @staticmethod
    def update_quality(items):
        name_class_map = {"Aged Brie": Brie,
                          "Backstage passes to a TAFKAL80ETC concert": BackstagePass,
                          "Sulfuras, Hand of Ragnaros": None,
                          "Conjured Mana Cake": Conjured
                          }
        for i in range(0, len(items)):
            object_name = Normal
            if items[i].name in name_class_map:
                object_name = name_class_map[items[i].name]

            if object_name:
                new_object = object_name(items[i])
                new_object.calc()
                items[i] = new_object
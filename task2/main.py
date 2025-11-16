from pymongo import MongoClient

from crud import *


client = MongoClient("mongodb://localhost:27017/")

db = client["cat_database"]
collection = db["cats"]



create_cat(collection, "barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
create_cat(collection, "murzik", 5, ["любить спати", "сіра шерсть"])

read_all_cats(collection)


read_cat_by_name(collection, "barsik")
update_cat_age(collection, "barsik", 4)
add_feature_to_cat(collection, "barsik", "муркоче голосно")


read_all_cats(collection)


delete_cat_by_name(collection, "murzik")
delete_all_cats(collection)

read_all_cats(collection)

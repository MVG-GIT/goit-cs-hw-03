from pprint import pprint

def create_cat(collection, name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Кота '{name}' успішно додано! ID: {result.inserted_id}")
    except Exception as e:
        print("Помилка при додаванні кота:", e)

def read_all_cats(collection):
    try:
        cats = list(collection.find())
        if cats:
            print("Усі коти:")
            for cat in cats:
                pprint(cat)
        else:
            print("Колекція порожня.")
    except Exception as e:
        print("Помилка при зчитуванні даних:", e)

def read_cat_by_name(collection, name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print("Знайдено кота:")
            pprint(cat)
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print("Помилка при пошуку кота:", e)

def update_cat_age(collection, name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print(f"Вік кота '{name}' оновлено до {new_age}.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print("Помилка при оновленні віку:", e)

def add_feature_to_cat(collection, name, new_feature):
    try:
        result = collection.update_one(
            {"name": name}, {"$addToSet": {"features": new_feature}}
        )
        if result.modified_count:
            print(f"Характеристика '{new_feature}' додана коту '{name}'.")
        else:
            print(f"Кота '{name}' не знайдено або така характеристика вже є.")
    except Exception as e:
        print("Помилка при додаванні характеристики:", e)

def delete_cat_by_name(collection, name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кота '{name}' видалено.")
        else:
            print(f"Кота '{name}' не знайдено.")
    except Exception as e:
        print("Помилка при видаленні кота:", e)

def delete_all_cats(collection):
    try:
        count = collection.delete_many({}).deleted_count
        print(f"Видалено {count} записів із колекції.")
    except Exception as e:
        print("Помилка при очищенні колекції:", e)

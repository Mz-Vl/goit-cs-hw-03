import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://user1:123456!@cluster0.wc5ktc7.mongodb.net/test")
db = client["test"]
collection = db["cats"]


# Create
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"New cat created with ID: {result.inserted_id}")


# Read
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)


def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat with name '{name}' not found.")


# Update
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Age updated for cat with name '{name}'.")
    else:
        print(f"Cat with name '{name}' not found.")


def add_cat_feature(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print(f"New feature '{new_feature}' added for cat with name '{name}'.")
    else:
        print(f"Cat with name '{name}' not found.")


# Delete
def delete_cat(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Cat with name '{name}' deleted.")
    else:
        print(f"Cat with name '{name}' not found.")


def delete_all_cats():
    result = collection.delete_many({})
    print(f"{result.deleted_count} cats deleted.")


# Example usage
if __name__ == "__main__":
    # Create
    create_cat("Barsik", 3, ["plays with toys", "loves to play"])
    create_cat("Murka", 8, ["plays with toys", "hate people"])
    create_cat("Tom", 7, ["plays with kids", "loves sleeping"])
    create_cat("Fluffy", 2, ["do not plays with people", "loves beaf"])

    # Read
    print("All cats:")
    read_all_cats()

    print("\nCat with name 'Barsik':")
    read_cat_by_name("Barsik")

    # Update
    update_cat_age("Barsik", 4)
    add_cat_feature("Barsik", "purrs loudly")

    # Delete
    delete_cat("Barsik")
    delete_all_cats()

def get_category():
    print("1. Food ")
    print("2. Books ")
    print("3. Travel ")
    print("4. Others ")
    c = input("Select a Category (1-4): ")
    cats = {"1": "Food", "2": "Books", "3": "Travel", "4": "Others"}
    return cats.get(c, "Invalid Category")

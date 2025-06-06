# מילון עם המוצרים הקיימים בחנות ומחירם
products = {
    "Milk": 5.90,
    "Bread": 3.50,
    "Eggs": 10.00,
    "Cheese": 12.30,
    "Apple": 2.20,
    "Banana": 3.10,
    "Chicken": 26.90,
    "Rice": 7.80,
    "Tomato": 4.50,
    "Cucumber": 3.80,
    "Yogurt": 4.20,
    "Coffee": 18.00,
    "Sugar": 6.50,
    "Water Bottle": 2.90,
    "Chocolate": 8.40
}

# עגלת קניות – מילון ריק שמתמלא לאורך הקנייה
cart = {}

# ====== פונקציה להצגת כל המוצרים הזמינים ======
def show_products():
    print("Available products:")
    for name in products:
        print(f"{name} - ${products[name]}")

# ====== פונקציה להוספת מוצרים לעגלה ברצף ======
def add_to_cart():
    print("Add products to cart (type 'done' to finish):")  # הסבר למשתמש איך להפסיק

    while True:  # לולאה שרצה כל עוד המשתמש לא סיים להוסיף
        name_input = input("Enter product name (or 'done' to finish): ")  # קלט של שם מוצר

        if name_input.lower() == "done":  # אם המשתמש סיים להוסיף מוצרים
            break  # יוצאים מהלולאה וחוזרים לתפריט הראשי

        matched_product = None  # ניצור משתנה שיחזיק את שם המוצר אם נמצא התאמה

        for name in products:  # נעבור על כל שם מוצר במילון המוצרים
            if name_input.lower() == name.lower():  # נשווה בלי תלות באותיות גדולות/קטנות
                matched_product = name  # שמרנו את השם בדיוק כמו שהוא מופיע במילון
                break  # יציאה מהלולאה – מצאנו התאמה

        if matched_product:  # אם נמצא מוצר מתאים
            quantity_input = input("Enter quantity: ")  # קלט של כמות

            if quantity_input.isdigit():  # נוודא שהקלט הוא מספר שלם
                quantity = int(quantity_input)  # נהפוך את הקלט למספר שלם

                if matched_product in cart:  # אם המוצר כבר קיים בעגלה
                    cart[matched_product]["quantity"] += quantity  # נוסיף לכמות הקיימת
                else:
                    cart[matched_product] = {  # אם המוצר לא בעגלה – נוסיף חדש
                        "quantity": quantity,  # נשמור את הכמות
                        "price": products[matched_product]  # ואת המחיר ממילון המוצרים
                    }

                print(f"{quantity} x {matched_product} added to cart.")  # הודעת הצלחה
            else:
                print("Invalid quantity.")  # אם הכמות לא מספר – הודעת שגיאה
        else:
            print("Product not found.")  # אם לא נמצא מוצר תואם – הודעת שגיאה


# ====== פונקציה להסרת מוצר מהעגלה ======
def remove_from_cart():
    name = input("Enter product name to remove: ")
    for item in cart:
        if name.lower() == item.lower():
            del cart[item]
            print("Product removed from cart.")
            return
    print("Product not found in cart.")

# ====== פונקציה לחיפוש מוצר בעגלה לפי שם חלקי ======
def search_in_cart():
    keyword = input("Enter product name to search: ")
    found = False
    for name in cart:
        if keyword.lower() in name.lower():
            q = cart[name]["quantity"]
            p = cart[name]["price"]
            print(f"{name} - Quantity: {q}, Price: ${p}")
            found = True
    if not found:
        print("No matching product found in cart.")

# ====== פונקציה להצגת כל העגלה כולל סכום וכמות ======
def show_cart():
    if not cart:
        print("Cart is empty.")
        return

    total = 0
    count = 0
    print("Cart contents:")
    for name in cart:
        q = cart[name]["quantity"]
        p = cart[name]["price"]
        print(f"{name} - Quantity: {q} - Price: ${p}")
        total += q * p
        count += q

    print("Total items:", count)
    print("Total price: $", round(total, 2))

# ====== פונקציה למיון מוצרים לפי מחיר בעגלה ======
def sort_cart_by_price():
    direction = input("Sort by price (asc/desc): ")
    if direction not in ["asc", "desc"]:
        print("Invalid option.")
        return

    reverse = True if direction == "desc" else False
    sorted_items = sorted(cart.items(), key=lambda x: x[1]["price"], reverse=reverse)

    for name, info in sorted_items:
        print(f"{name} - Quantity: {info['quantity']} - Price: ${info['price']}")

# ====== פונקציה לסינון מוצרים לפי מחיר ======
def filter_cart_by_price():
    option = input("1 - more than price, 2 - less than price: ")
    limit_input = input("Enter price: ")
    try:
        limit = float(limit_input)
    except ValueError:
        print("Invalid price.")
        return

    for name in cart:
        price = cart[name]["price"]
        if option == "1" and price > limit:
            print(f"{name} - ${price}")
        elif option == "2" and price < limit:
            print(f"{name} - ${price}")

# ====== פונקציית Checkout לסיום הקנייה ======
def checkout():
    show_cart()
    confirm = input("Confirm checkout? (yes/no): ")
    if confirm.lower() == "yes":
        cart.clear()
        print("Checkout complete.")

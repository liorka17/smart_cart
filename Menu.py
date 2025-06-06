# ייבוא של כל הפונקציות מקובץ functions.py
from functions import (
    show_products,      # הצגת כל המוצרים הקיימים
    add_to_cart,        # הוספת מוצר לעגלה
    remove_from_cart,   # הסרת מוצר מהעגלה
    search_in_cart,     # חיפוש מוצר בעגלה
    show_cart,          # הצגת כל העגלה
    sort_cart_by_price, # מיון מוצרים בעגלה לפי מחיר
    filter_cart_by_price, # סינון מוצרים לפי מחיר
    checkout            # סיום קנייה והצגת סיכום
)

# פונקציה שמריצה את התפריט הראשי בלולאה
def menu():
    while True:  # לולאה אינסופית – תיעצר רק כשנבחר לצאת
        # הדפסת תפריט
        print("\n===== MAIN MENU =====")
        print("1. Show available products")
        print("2. Add product to cart")
        print("3. Remove product from cart")
        print("4. Search product in cart")
        print("5. Show cart")
        print("6. Sort cart by price")
        print("7. Filter cart by price")
        print("8. Checkout (finish shopping)")
        print("9. Exit")

        # קלט מהמשתמש
        choice = input("Enter your choice (1-9): ")

        # בדיקה של הבחירה
        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            search_in_cart()
        elif choice == "5":
            show_cart()
        elif choice == "6":
            sort_cart_by_price()
        elif choice == "7":
            filter_cart_by_price()
        elif choice == "8":
            checkout()
        elif choice == "9":
            print("Goodbye!")  # יציאה מהמערכת
            break  # סיום הלולאה
        else:
            print("Invalid choice.")  # בחירה לא תקינה

# הרצת התפריט בפועל
menu()

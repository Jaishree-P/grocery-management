import mysql.connector
import time
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # <-- Change this to your MySQL password
    database="grocery_db"
)
cursor = conn.cursor()

# ---------------------- Admin Login ----------------------
def admin_login():
    print("\n🔐 Admin Login Required")
    username = input("👤 Username: ")
    password = input("🔑 Password: ")

    admin_user = "admin"
    admin_pass = "1234"

    if username == admin_user and password == admin_pass:
        print("✅ Login successful. Welcome Admin!\n")
        return True
    else:
        print("❌ Login failed. Invalid credentials.")
        return False

# ---------------------- Welcome Message ----------------------
def welcome():
    print("\n" + "*" * 50)
    print("🌟 Welcome to the Grocery Management System 🌟")
    print("*" * 50)
    
    time.sleep(2)
    print("📦 Track Products")
    print("🛒 Generate Customer Bills")
    print("📊 Manage Inventory Efficiently\n")
    time.sleep(2)

# ---------------------- Add Product ----------------------
def add_product():
    print("\n📝 Add New Product")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    conn.commit()
    print("✅ Product added successfully.\n")

# ---------------------- View Products ----------------------
def view_products():
    print("\n📋 Product List:")
    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()
    if not records:
        print("⚠️ No products found.\n")
    else:
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Price: ₹{row[2]} | Stock: {row[3]}")
    print()

# ---------------------- Update Product ----------------------
def update_product():
    print("\n✏️ Update Product")
    product_id = input("Enter product ID: ")
    print("1. Update price\n2. Update stock")
    choice = input("Choose option: ")
    if choice == "1":
        new_price = float(input("Enter new price: "))
        cursor.execute("UPDATE products SET price = %s WHERE id = %s", (new_price, product_id))
    elif choice == "2":
        new_stock = int(input("Enter new stock: "))
        cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (new_stock, product_id))
    else:
        print("❌ Invalid choice.")
        return
    conn.commit()
    print("✅ Product updated.\n")

# ---------------------- Delete Product ----------------------
def delete_product():
    print("\n🗑️ Delete Product")
    product_id = input("Enter product ID to delete: ")
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    print("✅ Product deleted.\n")

# ---------------------- Create Bill ----------------------
def create_bill():
    print("\n🧾 Create Customer Bill")
    customer_name = input("Enter customer name: ")
    items = []
    total = 0

    while True:
        view_products()
        pid = input("Enter product ID (or 0 to finish): ")
        if pid == '0':
            break
        qty = int(input("Enter quantity: "))
        cursor.execute("SELECT name, price, stock FROM products WHERE id = %s", (pid,))
        result = cursor.fetchone()
        if result:
            name, price, stock = result
            if stock >= qty:
                cost = price * qty
                total += cost
                items.append(f"{name} x{qty}")
                cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s", (qty, pid))
            else:
                print("⚠️ Insufficient stock.")
        else:
            print("❌ Product not found.")

    if items:
        items_str = ", ".join(items)
        cursor.execute("INSERT INTO bills (customer_name, items, total_amount) VALUES (%s, %s, %s)",
                       (customer_name, items_str, total))
        conn.commit()
        print(f"\n✅ Bill created for {customer_name}. Total: ₹{total}\n")
    else:
        print("❗ No items added to the bill.")

# ---------------------- View Bills ----------------------
def view_bills():
    print("\n📂 Customer Bills")
    cursor.execute("SELECT * FROM bills")
    records = cursor.fetchall()
    if not records:
        print("📭 No bills found.\n")
    else:
        for row in records:
            print(f"\n🧾 Bill ID: {row[0]}")
            print(f"👤 Customer: {row[1]}")
            print(f"📦 Items: {row[2]}")
            print(f"💰 Total: ₹{row[3]}")
            print(f"🕒 Time: {row[4]}")
    print()

# ---------------------- Goodbye Message ----------------------
def goodbye():
    print("\n🔚 Thank you for using Grocery Management System!")
    print("🚀 Keep managing smartly. Have a great day!\n")
    print("*" * 50)

# ---------------------- Menu ----------------------
def menu():
    welcome()
    while True:
        print("======== MAIN MENU ========")
        print("1️⃣ Add Product")
        print("2️⃣ View Products")
        print("3️⃣ Update Product")
        print("4️⃣ Delete Product")
        print("5️⃣ Create Customer Bill")
        print("6️⃣ View All Bills")
        print("7️⃣ Exit")
        print("===========================\n")

        choice = input("📌 Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            create_bill()
        elif choice == "6":
            view_bills()
        elif choice == "7":
            goodbye()
            break
        else:
            print("❌ Invalid choice. Please try again.\n")
        time.sleep(1)

# ---------------------- Entry Point ----------------------
if admin_login():
    menu()
else:
    print("🚫 Access Denied. Exiting the system.")

# Close DB connection
cursor.close()
conn.close()
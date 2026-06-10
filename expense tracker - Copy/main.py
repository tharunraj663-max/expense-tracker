import sqlite3

#Add Expense Function
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (DD-MM-YYYY): ")

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(amount, category, description, date) VALUES (?, ?, ?,?)",
        (amount, category, description, date)
    )

    conn.commit()
    conn.close()

    print("Expense added successfully!")

#View Expenses
def view_expenses():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    records = cursor.fetchall()

    for row in records:
        print(
            f"ID:{row[0]} | Amount: ₹{row[1]} | "
            f"Category: {row[2]} | Description: {row[3]} | Date: {row[4]}"
        )

    conn.close()

#Delete Expense
def delete_expense():
    expense_id = int(input("Enter expense ID to delete: "))

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()
    conn.close()

    print("Expense deleted!")

#update
def update_expense():
    expense_id = int(input("Enter Expense ID: "))
    new_amount = float(input("Enter new amount: "))
    new_category = input("Enter new category: ")
    new_description = input("Enter new description: ")
    new_date = input("Enter new date: (DD-MM-YYYY): ")

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount=?, category=?, description=?, date=?
        WHERE id=?
    """, (new_amount, new_category, new_description, new_date, expense_id))

    conn.commit()
    conn.close()

    print("Expense updated successfully!")

#Calculate Total Expenses
def total_expense():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    print("Total Expense:", total)

    conn.close()

#category
def category_summary():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    rows = cursor.fetchall()

    print("\nCategory Summary")
    for category, total in rows:
        print(f"{category}: ₹{total}")

    conn.close()

#totalexpense
def total_between_dates():
    start_date = input("Enter start date (DD-MM-YYYY): ")
    end_date = input("Enter end date (DD-MM-YYYY): ")

    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE date BETWEEN ? AND ?
    """, (start_date, end_date))

    total = cursor.fetchone()[0]

    if total is None:
        print("No expenses found in this date range.")
    else:
        print(f"Total Expense: ₹{total}")

    conn.close()

#import fun
import pandas as pd

def import_excel():
    try:
        df = pd.read_excel("expenses.xlsx")

        conn = sqlite3.connect("expense.db")

        df.to_sql(
            "expenses",
            conn,
            if_exists="append",
            index=False
        )

        conn.close()

        print("Excel data imported successfully!")

    except Exception as e:
        print("Error:", e)

#Create the Menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Total Expense")
    print("6. Category Summary")
    print("7. Total Between Dates")
    print("8. import Excel")
    print("9. exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        total_expense()

    elif choice == "6":
        category_summary()

    elif choice == "7":
        total_between_dates()

    elif choice == "8":
        import_excel()

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")



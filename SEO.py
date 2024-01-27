from tkinter import *
import sqlite3
import pandas as pd


def create_suppliers_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS suppliers
                (name TEXT, product_type TEXT, arrival_date TEXT)''')
    conn.commit()
    conn.close()


def save_suppliers_table():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM suppliers", conn)
    conn.close()
    df.to_excel('suppliers.xlsx', index=False)


def create_personnel_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS personnel
                (name TEXT, age INTEGER, phone_number TEXT, position TEXT)''')
    conn.commit()
    conn.close()


def save_personnel_table():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM personnel", conn)
    conn.close()
    df.to_excel('personnel.xlsx', index=False)


def create_products_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                (product_name TEXT, shelf_life INTEGER, purchase_price REAL, selling_price REAL)''')
    conn.commit()
    conn.close()


def save_products_table():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()
    df.to_excel('products.xlsx', index=False)


def create_transactions_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                (income REAL, expenses REAL, defective_items INTEGER, total_income REAL)''')
    conn.commit()
    conn.close()


def save_transactions_table():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    df.to_excel('transactions.xlsx', index=False)


def login():
    def open_main_menu():
        login_window.destroy()
        main_menu()

    login_window = Tk()
    login_window.title("Login")

    label_name = Label(login_window, text="ФИО:")
    label_name.pack()
    entry_name = Entry(login_window)
    entry_name.pack()

    label_organization = Label(login_window, text="Организация:")
    label_organization.pack()
    entry_organization = Entry(login_window)
    entry_organization.pack()

    button_login = Button(login_window, text="Войти", command=open_main_menu)
    button_login.pack()

    login_window.mainloop()


def main_menu():
    def open_main_functions_menu():
        main_menu_window.destroy()
        main_functions_menu()

    def open_transactions_menu():
        main_menu_window.destroy()
        transactions_menu()

    main_menu_window = Tk()
    main_menu_window.title("Main Menu")

    button_main_functions = Button(main_menu_window, text="Основные функции", command=open_main_functions_menu)
    button_main_functions.pack()

    button_transactions = Button(main_menu_window, text="Транзакции", command=open_transactions_menu)
    button_transactions.pack()

    button_exit = Button(main_menu_window, text="Выход", command=main_menu_window.quit)
    button_exit.pack()

    main_menu_window.mainloop()


def main_functions_menu():
    def open_suppliers_menu():
        main_functions_menu_window.destroy()
        suppliers_menu()

    def open_personnel_menu():
        main_functions_menu_window.destroy()
        personnel_menu()

    def open_products_menu():
        main_functions_menu_window.destroy()
        products_menu()

    main_functions_menu_window = Tk()
    main_functions_menu_window.title("Main Functions Menu")

    button_suppliers = Button(main_functions_menu_window, text="Поставщики", command=open_suppliers_menu)
    button_suppliers.pack()

    button_personnel = Button(main_functions_menu_window, text="Персонал", command=open_personnel_menu)
    button_personnel.pack()

    button_products = Button(main_functions_menu_window, text="Товары", command=open_products_menu)
    button_products.pack()

    button_back = Button(main_functions_menu_window, text="Назад", command=main_functions_menu_window.quit)
    button_back.pack()

    main_functions_menu_window.mainloop()


def suppliers_menu():
    def save_and_go_back():
        save_suppliers_table()
        suppliers_window.destroy()
        main_functions_menu()

    suppliers_window = Tk()
    suppliers_window.title("Suppliers")

    # Создание/проверка таблицы поставщиков в базе данных
    create_suppliers_table()

    label_name = Label(suppliers_window, text="Имя поставщика:")
    label_name.pack()
    entry_name = Entry(suppliers_window)
    entry_name.pack()

    label_product_type = Label(suppliers_window, text="Тип поставляемого товара:")
    label_product_type.pack()
    entry_product_type = Entry(suppliers_window)
    entry_product_type.pack()

    label_arrival_date = Label(suppliers_window, text="Дата привоза:")
    label_arrival_date.pack()
    entry_arrival_date = Entry(suppliers_window)
    entry_arrival_date.pack()

    button_save = Button(suppliers_window, text="Сохранить", command=save_and_go_back)
    button_save.pack()

    button_back = Button(suppliers_window, text="Назад", command=suppliers_window.quit)
    button_back.pack()

    suppliers_window.mainloop()


def personnel_menu():
    def save_and_go_back():
        save_personnel_table()
        personnel_window.destroy()
        main_functions_menu()

    personnel_window = Tk()
    personnel_window.title("Personnel")

    # Создание/проверка таблицы персонала в базе данных
    create_personnel_table()

    label_name = Label(personnel_window, text="ФИО:")
    label_name.pack()
    entry_name = Entry(personnel_window)
    entry_name.pack()

    label_age = Label(personnel_window, text="Возраст:")
    label_age.pack()
    entry_age = Entry(personnel_window)
    entry_age.pack()

    label_phone_number = Label(personnel_window, text="Номер телефона:")
    label_phone_number.pack()
    entry_phone_number = Entry(personnel_window)
    entry_phone_number.pack()

    label_position = Label(personnel_window, text="Должность:")
    label_position.pack()
    entry_position = Entry(personnel_window)
    entry_position.pack()

    button_save = Button(personnel_window, text="Сохранить", command=save_and_go_back)
    button_save.pack()

    button_back = Button(personnel_window, text="Назад", command=personnel_window.quit)
    button_back.pack()

    personnel_window.mainloop()


def products_menu():
    def save_and_go_back():
        save_products_table()
        products_window.destroy()
        main_functions_menu()

    products_window = Tk()
    products_window.title("Products")

    # Создание/проверка таблицы товаров в базе данных
    create_products_table()

    label_product_name = Label(products_window, text="Название товара:")
    label_product_name.pack()
    entry_product_name = Entry(products_window)
    entry_product_name.pack()

    label_shelf_life = Label(products_window, text="Срок хранения:")
    label_shelf_life.pack()
    entry_shelf_life = Entry(products_window)
    entry_shelf_life.pack()

    label_purchase_price = Label(products_window, text="Цена закупочная:")
    label_purchase_price.pack()
    entry_purchase_price = Entry(products_window)
    entry_purchase_price.pack()

    label_selling_price = Label(products_window, text="Цена продажи:")
    label_selling_price.pack()
    entry_selling_price = Entry(products_window)
    entry_selling_price.pack()

    button_save = Button(products_window, text="Сохранить", command=save_and_go_back)
    button_save.pack()

    button_back = Button(products_window, text="Назад", command=products_window.quit)
    button_back.pack()

    products_window.mainloop()


def transactions_menu():
    def save_and_go_back():
        save_transactions_table()
        transactions_window.destroy()
        main_menu()

    transactions_window = Tk()
    transactions_window.title("Transactions")

    # Создание/проверка таблицы транзакций в базе данных
    create_transactions_table()

    label_income = Label(transactions_window, text="Доходы:")
    label_income.pack()
    entry_income = Entry(transactions_window)
    entry_income.pack()

    label_expenses = Label(transactions_window, text="Расходы:")
    label_expenses.pack()
    entry_expenses = Entry(transactions_window)
    entry_expenses.pack()

    label_defective_items = Label(transactions_window, text="Кол-во брака (стоимость):")
    label_defective_items.pack()
    entry_defective_items = Entry(transactions_window)
    entry_defective_items.pack()

    label_total_income = Label(transactions_window, text="Общий доход:")
    label_total_income.pack()
    entry_total_income = Entry(transactions_window)
    entry_total_income.pack()

    button_save = Button(transactions_window, text="Сохранить", command=save_and_go_back)
    button_save.pack()

    button_back = Button(transactions_window, text="Назад", command=transactions_window.quit)
    button_back.pack()

    transactions_window.mainloop()


login()

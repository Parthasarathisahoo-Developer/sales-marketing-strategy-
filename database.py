import sqlite3

def connect():
    return sqlite3.connect("sales.db", check_same_thread=False)

def create_table():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL,
        date TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def insert_data(product, quantity, price, date):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
                   (product, quantity, price, date))
    
    conn.commit()
    conn.close()

def view_data():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

# ✏️ UPDATE
def update_data(id, product, quantity, price, date):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
    UPDATE sales
    SET product=?, quantity=?, price=?, date=?
    WHERE id=?
    """, (product, quantity, price, date, id))
    
    conn.commit()
    conn.close()

# ❌ DELETE
def delete_data(id):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM sales WHERE id=?", (id,))
    
    conn.commit()
    conn.close()
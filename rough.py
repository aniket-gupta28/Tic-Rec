import sqlite3

with sqlite3.connect('database.db') as conn:
    cur = conn.cursor()
    cur.execute('DELETE FROM sales WHERE userId = 1')
    conn.commit()
conn.close()

# with sqlite3.connect('database.db') as conn:
#     cur = conn.cursor()
#     cur.execute("UPDATE products SET name = ? WHERE productId = ?", ('Captain America',8))
#     conn.commit()
# conn.close()
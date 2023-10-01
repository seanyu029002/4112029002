import sqlite3

con = sqlite3.connect('BBQ.db')

cursor = con.cursor()

cursor.execute("INSERT INTO ingredients VALUES(1, 'chicken', 30, 5)")
cursor.execute("INSERT INTO ingredients VALUES(2, 'beef', 55, 10)")
cursor.execute("INSERT INTO ingredients VALUES(3, 'pork', 40, 15)")

cursor.execute("UPDATE ingredients SET price = 35 WHERE name = 'pork' ")
cursor.execute("UPDATE ingredients SET quantity = 40 WHERE name = 'chicken' ")

cursor.execute("DELETE FROM ingredients WHERE price = '40'")

cursor.execute("SELECT * FROM ingredients")
ingredients = cursor.fetchall() 

for ingredient in ingredients:
    print(ingredient)


cursor.close()
con.commit()
con.close()

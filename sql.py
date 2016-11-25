import sqlite3

with sqlite3.connect("formData.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE postData(name TEXT, message TEXT)""")
    c.execute('INSERT INTO postData VALUES("Patrick", "I think Spurs Will win the league!!.")')
    c.execute('INSERT INTO postData VALUES("Gerry", "I also think that. Also Harry Kane will be top goalscorer again!")')
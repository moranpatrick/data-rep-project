import sqlite3

with sqlite3.connect("data/formData.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE postData(name TEXT, message TEXT)""")
    c.execute('INSERT INTO postData VALUES("Patrick", "I think Spurs Will win the league!!.")')
    c.execute('INSERT INTO postData VALUES("Gerry", "I also think that. Also Harry Kane will be top goalscorer again!")')

    c.execute("""CREATE TABLE teamData(position TEXT, names TEXT)""")
    c.execute('INSERT INTO teamData VALUES("GoalKeeper", "Hugo Lloris")')
    c.execute('INSERT INTO teamData VALUES("BackLine", "testest")')
    c.execute('INSERT INTO teamData VALUES("Mid-Field", "test, test ,test ,test")')
    c.execute('INSERT INTO teamData VALUES("Forwards", "test, test ,test ,test")')
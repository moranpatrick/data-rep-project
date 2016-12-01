import sqlite3 #import sqlite3
#Create Database  formData.db
with sqlite3.connect("data/formData.db") as connection:
    c = connection.cursor()
    #create 2 tables with default data
    c.execute("""CREATE TABLE postData(name TEXT, message TEXT)""")
    c.execute('INSERT INTO postData VALUES("Patrick", "I think Spurs Will win the league!!.")')
    c.execute('INSERT INTO postData VALUES("Gerry", "I also think that. Also Harry Kane will be top goalscorer again!")')

    c.execute("""CREATE TABLE teamData(position TEXT, names TEXT)""")
    c.execute('INSERT INTO teamData VALUES("GOALKEEPER", "Lloris")')
    c.execute('INSERT INTO teamData VALUES("BACKLINE", "Walker   McAuley   Coleman")')
    c.execute('INSERT INTO teamData VALUES("MIDFIELD", "Sacnchez   Hazard   Coutinhio   Mata")')
    c.execute('INSERT INTO teamData VALUES("FORWARDS", "Defo   Kane   Aguero")')
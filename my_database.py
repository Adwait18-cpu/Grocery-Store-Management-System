import sqlite3


def create():
    """ Function to create and establish a connection with Database file. """
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY, name TEXT, phone_number TEXT, "
                "address TEXT, purchase TEXT, credit TEXT, cdate TEXT )")
    con.commit()
    con.close()


def display():
    """ Function to display all the records in database """
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows


def search(name="", phone_number=""):
    """ Function to search a particular record """
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    con.execute("SELECT * FROM account WHERE name=? OR phone_number=?", (name, phone_number))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows


def add(name, phone_number, address, purchase, credit, cdate):
    """ Function to add a new record """
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL, ?, ?, ?, ?, ?, ?)",
                (name, phone_number, address, purchase, credit, cdate))
    con.commit()
    con.close()


def update(id, name, phone_number, address, purchase, credit, cdate):
    """ Function to update existing record """
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET name=?, phone_number=?, address=?, purchase=?, credit=?, cdate=? WHERE id=?",
                (name, phone_number, address, purchase, credit, cdate, id))
    con.commit()
    con.close()


def delete(id):
    """ Function to delete a selected record """
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?", (id,))
    con.commit()
    con.close()


create()

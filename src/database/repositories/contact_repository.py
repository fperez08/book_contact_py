from .repositories_interfaces import IRepository
import sqlite3


class ContactRepository(IRepository):
    def __init__(self, database_name):
        # initialize database connection
        self._connection_string = database_name
        self._connection = sqlite3.connect(database_name)
        self.__create_table()

    def __create_table(self):
        cursor = self._connection.cursor()
        cursor.execute(
            """
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT
    )
"""
        )

    def get_all(self):
        # query all records from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        return results

    def get_by_id(self, id):
        # query record by id from database
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id=?", (id,))
        result = cursor.fetchone()
        return result if result is not None else None

    def create(self, contact):
        # insert record into database
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO contacts(name, phone, email) VALUES (?, ?, ?)",
            (contact["name"], contact["phone"], contact["email"]),
        )
        self._connection.commit()
        contact["id"] = cursor.lastrowid
        return contact

    def update(self, contact):
        # update record in database
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
            (contact["name"], contact["phone"], contact["email"], contact["id"]),
        )
        self._connection.commit()
        return cursor.rowcount > 0

    def delete(self, id):
        # delete record from database
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id=?", (id,))
        self._connection.commit()
        return cursor.rowcount > 0

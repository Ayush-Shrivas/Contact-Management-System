# database.py
import sqlite3

class Database:
    def __init__(self, db_file):
        """Initialize db class variables"""
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS contact_book (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT
            )
        """)
        self.conn.commit()

    def fetch_all(self):
        """Fetch all contacts from the database"""
        self.cur.execute("SELECT * FROM contact_book ORDER BY name ASC")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, phone, email, address):
        """Insert a new contact into the database"""
        self.cur.execute("INSERT INTO contact_book VALUES (NULL, ?, ?, ?, ?)",
                         (name, phone, email, address))
        self.conn.commit()

    def remove(self, contact_id):
        """Remove a contact from the database"""
        self.cur.execute("DELETE FROM contact_book WHERE id = ?", (contact_id,))
        self.conn.commit()

    def update(self, contact_id, name, phone, email, address):
        """Update a contact in the database"""
        self.cur.execute("""
            UPDATE contact_book
            SET name = ?, phone = ?, email = ?, address = ?
            WHERE id = ?
        """, (name, phone, email, address, contact_id))
        self.conn.commit()

    def search(self, query):
        """Search for contacts by name or phone"""
        self.cur.execute("""
            SELECT * FROM contact_book WHERE name LIKE ? OR phone LIKE ?
        """, ('%' + query + '%', '%' + query + '%'))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        """Close the database connection"""
        self.conn.close()
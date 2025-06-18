import sqlite3

class Quiz:

    def __init__(self):
        self.connect = sqlite3.connect("quiz.db")
        self.create_table()


    def create_table(self):
        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS questions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            correct INTEGER )
            """
        )
        self.connect.commit()

    def add_question(self, question, option, correct):

        self.connect.execute("""

        INSERT INTO questions(question, option1, option2, option3, option4, correct)
                             VALUES(?,?,?,?,?,?)
        """, (question, *option, correct))
        self.connect.commit()


    def fetch_question(self):
        fetched = self.connect.execute("""
            
        SELECT * FROM questions
        """)
        return fetched.fetchall()



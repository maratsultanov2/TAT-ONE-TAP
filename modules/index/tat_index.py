import sqlite3
from datetime import datetime

class TATIndex:
    def __init__(self, db_path='tat_index.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('CREATE TABLE IF NOT EXISTS dialogues (id TEXT PRIMARY KEY, timestamp TEXT, topics TEXT, summary TEXT, importance TEXT, linked_chunks TEXT)')
        self.conn.commit()

    def add(self, dialog_id, topics, summary, importance='normal'):
        self.conn.execute('INSERT OR REPLACE INTO dialogues VALUES (?, ?, ?, ?, ?, ?)', (dialog_id, datetime.now().isoformat(), topics, summary, importance, None))
        self.conn.commit()

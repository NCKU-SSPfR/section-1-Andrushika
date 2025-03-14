import sqlite3

DB_NAME = "game.db"


def initialize():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create game_state table (with username column)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS game_state (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        current_level_name TEXT NOT NULL,
        map_size TEXT NOT NULL,
        health INTEGER NOT NULL,
        path TEXT NOT NULL,
        current_position TEXT NOT NULL
    )
    """
    )

    conn.commit()
    conn.close()

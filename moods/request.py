import sqlite3
import json
from models import Mood

def get_all_moods():
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      m.id,
      m.label
    FROM Mood m
    """)

    moods = []
    dataset = db_cursor.fetchall()

    for data in dataset:
      mood = Mood(data["id"], data["label"])

      moods.append(mood.__dict__)

    return json.dumps(moods)


from models import Tag
import sqlite3
import json

def get_all_tags():
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      t.id,
      t.subject
    FROM Tag t
    """)

    tags = []
    dataset = db_cursor.fetchall()

    for data in dataset:
      tag = Tag(data["id"], data["subject"])

      tags.append(tag.__dict__)

    return json.dumps(tags)

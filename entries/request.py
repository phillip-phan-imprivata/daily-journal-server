import sqlite3
import json
from models import Entry
from models import Mood
from models import Tag

def get_all_entries():
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.date,
      e.entry,
      e.concept,
      e.instructor_id,
      e.mood_id,
      m.label mood_label,
      et.tag_id tag_id,
      t.subject tag_subject
    FROM Entry e
    JOIN Mood m
      ON m.id = e.mood_id
    JOIN Entry_Tag et
      ON et.entry_id = e.id
    JOIN Tag t
      ON t.id = et.tag_id 
    """)

    entries = []
    used_id = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      new_entry = Entry(row["id"], row["date"], row["entry"], row["concept"], row["instructor_id"], row["mood_id"])
      mood = Mood(row["mood_id"], row["mood_label"])
      tag = Tag(row["tag_id"], row["tag_subject"])

      entry_id = new_entry.__dict__["id"]
      found_id = None

      try:
        found_id = used_id.index(entry_id)
      except IndexError:
        pass
      except ValueError:
        pass

      if found_id != None:
        for entry in entries:
          if entry["id"] == entry_id:
            entry["tags"].append(tag.__dict__)
      else:
        used_id.append(entry_id)
        new_entry.mood = mood.__dict__
        new_entry.tags.append(tag.__dict__)
        entries.append(new_entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.date,
      e.entry,
      e.concept,
      e.instructor_id,
      e.mood_id
    FROM Entry e
    WHERE e.id = ?
    """, (id, ))

    data = db_cursor.fetchone()

    entry = Entry(data["id"], data["date"], data["entry"], data["concept"], data["instructor_id"], data["mood_id"])
    
    return json.dumps(entry.__dict__)

def delete_entry(id):
  with sqlite3.connect("./dailyjournal.db") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    DELETE FROM Entry
    WHERE id = ?
    """, (id, ))

def get_searched_entry(search):
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.date,
      e.entry,
      e.concept,
      e.instructor_id,
      e.mood_id
    FROM Entry e
    WHERE e.entry LIKE ?
    """, ("%" + search + "%", ))

    entries = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      entry = Entry(row["id"], row["date"], row["entry"], row["concept"], row["instructor_id"], row["mood_id"])
      entries.append(entry.__dict__)

  return json.dumps(entries)

def create_entry(new_entry):
  with sqlite3.connect("./dailyjournal.db") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    INSERT INTO Entry
      (date, entry, concept, instructor_id, mood_id)
    VALUES
      (?, ?, ?, ?, ?);
    """, (new_entry["date"], new_entry["entry"], new_entry["concept"], new_entry["instructor_id"], new_entry["mood_id"]))
    
    id = db_cursor.lastrowid

    for tag in new_entry["entry_tags"]:
      db_cursor.execute("""
      INSERT INTO Entry_Tag
        (entry_id, tag_id)
      VALUES
        (?, ?)
      """, (id, tag))

    new_entry["id"] = id

  return json.dumps(new_entry)

def update_entry(id, new_entry):
  with sqlite3.connect("./dailyjournal.db") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    UPDATE Entry
      SET
        date = ?,
        entry = ?,
        concept = ?,
        instructor_id = ?,
        mood_id = ?
    WHERE id = ?
    """, (new_entry["date"], new_entry["entry"], new_entry["concept"], new_entry["instructor_id"], new_entry["mood_id"], id, ))

    rows_affected = db_cursor.rowcount

  if rows_affected == 0:
    return False
  else:
    return True
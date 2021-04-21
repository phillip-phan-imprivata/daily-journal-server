class Entry():
  def __init__(self, id, date, entry, concept, instructor_id, mood_id):
    self.id = id
    self.date = date
    self.entry = entry
    self.concept = concept
    self.instructor_id = instructor_id
    self.mood_id = mood_id
    self.mood = None
    self.tags = []

CREATE TABLE 'Entry' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'date' TEXT NOT NULL,
  'entry' TEXT NOT NULL,
  'concept' TEXT NOT NULL,
  'instructor_id' INTEGER NOT NULL,
  'mood_id' INTEGER NOT NULL,
  FOREIGN KEY(`instructor_id`) REFERENCES `Instructors`(`id`),
  FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE 'Tag' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'subject' TEXT NOT NULL
);

CREATE TABLE 'Entry_Tag' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'entry_id' INTEGER NOT NULL,
  'tag_id' INTEGER NOT NULL,
  FOREIGN KEY('entry_id') REFERENCES 'Entries'('id'),
  FOREIGN KEY('tag_id') REFERENCES 'Tags'('id')
);

CREATE TABLE 'Mood' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'label' TEXT NOT NULL
);

CREATE TABLE 'Instructor' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'name' TEXT NOT NULL
)

INSERT INTO `Mood` VALUES (null, 'Good');
INSERT INTO `Mood` VALUES (null, 'Bad');
INSERT INTO `Mood` VALUES (null, 'Sad');
INSERT INTO `Mood` VALUES (null, 'Ok');
INSERT INTO `Mood` VALUES (null, 'Not Ok');

INSERT INTO `Instructor` VALUES (null, 'Jisie');
INSERT INTO `Instructor` VALUES (null, 'Hannah');
INSERT INTO `Instructor` VALUES (null, 'Scott');
INSERT INTO `Instructor` VALUES (null, 'Adam');

INSERT INTO `Tag` VALUES (null, 'html');
INSERT INTO `Tag` VALUES (null, 'css');
INSERT INTO `Tag` VALUES (null, 'js');

INSERT INTO `Entry` VALUES (null, '2021-2-17', 'what is going on', 'life', 1, 5);
INSERT INTO `Entry` VALUES (null, '2021-2-18', 'oh okay', 'me', 2, 5);

INSERT INTO `Entry_Tag` VALUES (null, 1, 1);
INSERT INTO `Entry_Tag` VALUES (null, 1, 2);
INSERT INTO `Entry_Tag` VALUES (null, 2, 1);

SELECT
      e.id,
      e.date,
      e.entry,
      e.concept,
      e.instructor_id,
      e.mood_id,
      m.label mood_label
    FROM Entry e
    JOIN Mood m
      ON m.id = e.mood_id


SELECT * 
FROM Tag

SELECT *
FROM Mood

    SELECT 
      DISTINCT e.id,
      e.date,
      e.entry,
      e.concept,
      e.instructor_id,
      e.mood_id,
      m.label mood_label,
      et.tag_id tag_id
    FROM Entry e
    JOIN Mood m
      ON m.id = e.mood_id
    JOIN Entry_Tag et
      ON et.entry_id = e.id
    JOIN Tag t
      ON t.id = et.tag_id

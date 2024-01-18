-- lists all records of the table second_table of the database
SELECT score, name FROM second_table
WHERE name IS NOT NULL and name != ''
ORDER BY score DESC;

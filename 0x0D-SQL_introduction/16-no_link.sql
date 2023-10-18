-- lists all records of the second_table of database
SELECT score, name
FROM second_table
WHERE EXISTS (SELECT name FROM second_table)
ORDER BY score DESC;

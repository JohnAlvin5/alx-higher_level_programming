-- lists all records of the second_table of database
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;

-- List all records with a valid name (not NULL, not empty)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != 
ORDER BY score DESC;

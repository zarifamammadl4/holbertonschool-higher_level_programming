-- 16-no_link.sql
-- List all records with a name, display score and name, sorted by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != 
ORDER BY score DESC;

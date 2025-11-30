-- This script lists all records with non-empty names
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != 
ORDER BY score DESC;

-- 8-cities_of_california_subquery.sql
-- This script lists all cities of California, sorted by city id.
-- The query avoids using JOIN and uses a subquery instead.

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;

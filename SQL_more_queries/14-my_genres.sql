-- 14-my_genres.sql
-- List all genres of the TV show "Dexter", sorted by genre name.

SELECT g.name
FROM genres AS g
JOIN tv_show_genres AS tsg ON g.id = tsg.genre_id
JOIN tv_shows AS tv ON tv.id = tsg.show_id
WHERE tv.title = 'Dexter'
ORDER BY g.name ASC;

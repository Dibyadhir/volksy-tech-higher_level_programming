-- task-10
SELECT S.title,G.genre_id
FROM tv_shows AS S
INNER JOIN tv_show_genres AS G
ON S.id = G.show_id
ORDER BY S.title, G.genere_id;

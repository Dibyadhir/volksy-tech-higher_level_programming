-- task-20
SELECT name,SUM(rate) AS rating 
FROM tv_genres 
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
inner join tv_show_ratings on tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name 
ORDER BY rating DESC;

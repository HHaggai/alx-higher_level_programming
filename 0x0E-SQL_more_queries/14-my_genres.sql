-- uses the hbtn_0d_tvshows databse to lists all the genrs of the show Dexter
-- uses databse to lsts all the rows in a table correspondin to all the rows in another
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC

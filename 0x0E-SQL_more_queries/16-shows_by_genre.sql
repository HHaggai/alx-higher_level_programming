-- lists all the shows, and all the genrs linkd to that show, from the datbase hbtn_0d_tvshows
-- lists all the rows of a tabl linkd to another table
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;

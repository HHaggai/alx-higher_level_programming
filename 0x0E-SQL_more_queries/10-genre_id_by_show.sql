-- lists all the shows containd in hbtn_0d_tvshows that have at least one genre linkd
-- lists all the rows of a databse with one column in common
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

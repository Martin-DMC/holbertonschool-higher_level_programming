-- lists all shows contained in the database hbtn_0d_tvshow
SELECT s.title, g.genre_id FROM tv_shows AS s LEFT JOIN tv_show_genres AS g ON g.show_id = s.id ORDER BY title, genre_id ASC;
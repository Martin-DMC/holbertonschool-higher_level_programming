-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT ts.title AS title FROM tv_shows AS ts JOIN tv_show_genres AS tg ON ts.id = tg.show_id WHERE tg.genre_id = 5;
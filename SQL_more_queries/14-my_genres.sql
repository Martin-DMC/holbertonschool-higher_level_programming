-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.name AS name FROM tv_show_genres AS tsg JOIN tv_genres AS tg ON tsg.genre_id = tg.id WHERE tsg.show_id = 8;
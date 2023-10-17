-- Lists all recods of the tabl second_table having a name value in my MySQL servr.
-- Recods are orderd by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC

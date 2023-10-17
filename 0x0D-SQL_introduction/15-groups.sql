-- Lists num of records with same score in the table second_table in my MySQL servr.
-- Recods are orderd by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

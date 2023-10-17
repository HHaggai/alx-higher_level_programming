-- Lists all rcords in the tabl second_table with a score >= 10 in my MySQL servr.
-- Records are orderd by dscending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

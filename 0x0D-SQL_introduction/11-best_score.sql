-- Lists all recrds with a score >= 10 in the table second_table
SELECT name, score FROM second_table
WHERE score >= 10
ORDER BY score DESC;

-- Script that lists all records with a score >= in second_table in MySQL server
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
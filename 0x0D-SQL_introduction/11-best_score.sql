-- A script that lists all records with the score>= 10 in the second_table in the database

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

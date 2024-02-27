-- A script that lists the number of records with the same score in the table 
-- second_table on the database hbtn_0c_0 in the Mysql server

SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number`DESC;

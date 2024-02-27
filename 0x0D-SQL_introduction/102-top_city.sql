-- A script that displays the top 3 of cities temparature
-- during July and August ordered b temperature in descending order

SELECT `city`, AVG(`value`) 'avg_temp' FROM `temperatures` WHERE `month` = 7 OR `month = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;

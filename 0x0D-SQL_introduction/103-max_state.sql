-- A script to display the max temp of each state ordered by state name

SELECT `state`, MAX(`value`) 'max_temp' FROM `temperatures` GROUP BY `state` ORDER BY `state` ASC;

-- displays the top 3 of cities temp during july and august ordered by temp
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE `month` = 7 OR `month` = 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;

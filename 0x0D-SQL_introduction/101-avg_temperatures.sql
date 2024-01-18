-- display the average temp by city order
SELECT city, AVG(value) AS average FROM temperatures GROUP BY city
ORDER BY average DESC;

-- task 20
SELECT DISTINCT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

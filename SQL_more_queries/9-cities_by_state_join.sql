-- task-9
SELECT cities.id,cities.name,states.name
FROM cities 
INNER JOINS states ON cities.state_id = states.id
ORDER BY cities.id;

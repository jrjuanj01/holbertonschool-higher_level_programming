-- Block
SELECT cities.id,
    cities.name,
    states.name
FROM cities
    INNER JOIN states USING (states.id)
ORDER BY cities.id ASC;
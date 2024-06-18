-- Block
SELECT id,
    name
FROM cities
    INNER JOIN states USING (name)
ORDER BY id ASC;
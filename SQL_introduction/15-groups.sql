-- Block
SELECT score,
    COUNT(*)
FROM second_table
GROUP BY score
HAVING COUNT(*) > 1
ORDER BY score DESC;
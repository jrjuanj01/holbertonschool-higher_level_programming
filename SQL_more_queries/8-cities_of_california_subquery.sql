-- Block
SELECT name
FROM hbtn_0d_2.cities
WHERE state_id = (
        SELECT id
        FROM hbtn_0d_2.states
        WHERE name = California
    );
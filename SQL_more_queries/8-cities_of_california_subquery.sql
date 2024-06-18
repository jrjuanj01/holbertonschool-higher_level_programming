-- Block
SELECT name
FROM hbtn_0d_2.cities
WHERE state_id = (
        SELECT state_id
        FROM hbtn_0d_2.states
        WHERE name = California
    );
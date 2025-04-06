SELECT p.id AS ID, COUNT(c.id) AS CHILD_COUNT
FROM ecoli_data AS p
LEFT JOIN ecoli_data AS c
ON p.id=c.parent_id
GROUP BY p.id ORDER BY p.id;

-- SELECT p.id as PID, c.id as CID
-- FROM ecoli_data AS p
-- LEFT JOIN ecoli_data as c
-- ON p.id=c.parent_id
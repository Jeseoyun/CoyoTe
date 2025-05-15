SELECT e1.id
FROM ecoli_data AS e1
    JOIN ecoli_data AS e2 ON e1.parent_id = e2.id
    JOIN ecoli_data AS e3 ON e2.parent_id = e3.id
WHERE e3.parent_id IS NULL
ORDER BY e1.id ASC
SELECT ecoli1.id AS ID, COUNT(ecoli2.id) as CHILD_COUNT
FROM ecoli_data AS ecoli1
LEFT JOIN
ecoli_data AS ecoli2
ON ecoli1.id = ecoli2.parent_id
GROUP BY ecoli1.id;
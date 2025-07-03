WITH per AS (
    SELECT id, PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) as per_rank
    FROM ECOLI_DATA
)
SELECT id,
CASE
    WHEN per_rank < 0.25 THEN 'CRITICAL'
    WHEN per_rank < 0.5 THEN 'HIGH'
    WHEN per_rank < 0.75 THEN 'MEDIUM'
    ELSE 'LOW'
END AS colony_name
FROM per
ORDER BY id;

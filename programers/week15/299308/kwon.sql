WITH quarter AS (
    SELECT 
        CASE
            WHEN(QUARTER(differentiation_date)) = 1 THEN '1Q'
            WHEN(QUARTER(differentiation_date)) = 2 THEN '2Q'
            WHEN(QUARTER(differentiation_date)) = 3 THEN '3Q'
            WHEN(QUARTER(differentiation_date)) = 4 THEN '4Q'
            ELSE NULL
    END AS quarter
    FROM ecoli_data
)

SELECT quarter, COUNT(*) AS ecoli_count
FROM quarter
GROUP BY quarter
ORDER BY quarter
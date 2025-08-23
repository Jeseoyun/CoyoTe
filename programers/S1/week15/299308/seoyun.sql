-- SELECT CONCAT(QUARTER(differentiation_date), 'Q') AS quarter, COUNT(*) AS ecoli_count
-- FROM ecoli_data
-- GROUP BY QUARTER(differentiation_date)
-- ORDER BY QUARTER(differentiation_date);

WITH quarter_data AS (
  SELECT QUARTER(differentiation_date) AS quarter
  FROM ecoli_data
)

SELECT CONCAT(quarter, 'Q') AS quarter, COUNT(*) AS ecoli_count
FROM quarter_data
GROUP BY quarter
ORDER BY quarter;
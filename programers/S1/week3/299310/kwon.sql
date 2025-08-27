SELECT year(differentiation_date) AS YEAR,
(
    SELECT MAX(size_of_colony) FROM ecoli_data
    WHERE year(differentiation_date) = year
) - size_of_colony AS YEAR_DEV,
ID
FROM ECOLI_DATA
ORDER BY YEAR, YEAR_DEV
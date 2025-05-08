# 대장균의 크기에 따라 분류하기 2

# size_of_colony의 크기에 따라 내림차순으로 정렬 후 NTILE 함수를 사용하여 25%씩 4분할
SELECT
    id,
    CASE NTILE(4) OVER (ORDER BY size_of_colony DESC)
        WHEN 1 THEN 'CRITICAL'
        WHEN 2 THEN 'HIGH'
        WHEN 3 THEN 'MEDIUM'
        WHEN 4 THEN 'LOW'
    END AS colony_name
FROM ecoli_data
ORDER BY id;


# 옛날 풀이
WITH RANK_DATA AS (
    SELECT ID,
        PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS SIZE_RANK
    FROM `ECOLI_DATA`
)
SELECT ID, 
    CASE 
        WHEN RD.SIZE_RANK <= 0.25 THEN "CRITICAL"
        WHEN RD.SIZE_RANK <= 0.50 THEN "HIGH"
        WHEN RD.SIZE_RANK <= 0.75 THEN "MEDIUM"
        ELSE "LOW"
    END AS COLONY_NAME
FROM `ECOLI_DATA` AS ED
LEFT JOIN `RANK_DATA` AS RD
USING (ID)
ORDER BY ID ASC;
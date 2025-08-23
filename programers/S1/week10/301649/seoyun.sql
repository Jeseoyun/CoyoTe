-- 1. 전체 데이터 개수 구하기
-- 2. 내림 차순으로 정렬
-- 3. 행 수에 따라 분기하기

WITH total_data AS (
    SELECT COUNT(*) as total
    FROM ecoli_data
),
ranked_data AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY size_of_colony DESC) AS row_num
    FROM ecoli_data
)

SELECT r.id, (
    CASE
        WHEN r.row_num <= t.total * 0.25 THEN 'CRITICAL'
        WHEN r.row_num <= t.total * 0.5 THEN 'HIGH'
        WHEN r.row_num <= t.total * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END
    ) AS colony_name
FROM ranked_data as r, total_data as t
ORDER BY r.id;
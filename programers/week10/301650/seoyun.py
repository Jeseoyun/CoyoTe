-- 1. root인놈들 구해서 오른쪽에 2세대, 3세대 붙인다
-- 2. 3세대 id에 대해 오름차순 정렬

WITH root AS (
    SELECT *
    FROM ecoli_data
    WHERE parent_id IS NULL
)

SELECT g3.id as id
FROM root AS g1
    LEFT JOIN ecoli_data AS g2
    ON g1.id=g2.parent_id

    LEFT JOIN ecoli_data AS g3
    ON g2.id=g3.parent_id
WHERE g3.id IS NOT NULL
ORDER BY g3.id;
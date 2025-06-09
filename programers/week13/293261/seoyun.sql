-- 1. 종류별로 가장 큰 물고기 찾기
-- 2. 그놈의 id, 이름을 찾기위해 JOIN하기

WITH largest_fish AS (
    SELECT fish_type, MAX(length) AS length
    FROM fish_info
    GROUP BY fish_type
)
SELECT fish_info.id, fish_name_info.fish_name, largest_fish.length
FROM largest_fish
    JOIN fish_name_info
        ON largest_fish.fish_type=fish_name_info.fish_type
    JOIN fish_info
        ON (largest_fish.length=fish_info.length AND largest_fish.fish_type=fish_info.fish_type)
ORDER BY fish_info.id;
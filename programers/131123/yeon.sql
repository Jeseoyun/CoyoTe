# 즐겨찾기가 가장 많은 식당 정보 출력하기 

SELECT ri.food_type, ri.rest_id, ri.rest_name, ri.favorites
FROM rest_info AS ri 
INNER JOIN (
    SELECT food_type, MAX(favorites) AS max_favorites
    FROM rest_info
    GROUP BY food_type
) AS mf 
ON ri.food_type = mf.food_type and ri.favorites = mf.max_favorites
ORDER BY food_type DESC;
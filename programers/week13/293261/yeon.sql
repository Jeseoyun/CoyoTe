# 물고기 중류 별 대어 찾기 
# https://school.programmers.co.kr/learn/courses/30/lessons/293261

--  fish_info 테이블에서 물고기 종류별로 가장 긴 물고기를 찾고,
WITH max_length AS (
    SELECT fish_type, MAX(length) AS max_length
    FROM fish_info 
    GROUP BY fish_type
)

# fish_info 와 fish_name_info 테이블을 조인하여 물고기 이름을 가져온 후,
# max_length 테이블과 조인하여 종류 별로 가장 긴 물고기를 찾는다.
SELECT fi.id, fni.fish_name, length
FROM fish_info AS fi 
LEFT JOIN fish_name_info AS fni 
ON fi.fish_type = fni.fish_type
LEFT JOIN max_length AS ml 
ON fi.fish_type = ml.fish_type 
WHERE fi.length = ml.max_length
ORDER BY fi.id ;
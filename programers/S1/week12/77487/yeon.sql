# 헤비 유저가 소유한 장소
# https://school.programmers.co.kr/learn/courses/30/lessons/77487


-- 헤비 유저가 소유한 장소를 찾기 위해 places 테이블에서 host_id를 기준으로 그룹화하고, 해당 host_id가 2개 이상의 장소를 소유한 경우만을 필터링
WITH hv_hst_id AS (
    SELECT host_id
    FROM places 
    GROUP BY host_id
    HAVING count(id) >= 2
)

-- 이후 places 테이블과 hv_hst_id CTE를 RIGHT JOIN하여 헤비 유저가 소유한 장소의 정보를 가져움
-- RIGHT JOIN 을 하는 이유는 hv_hst_id CTE에 있는 host_id가 기준이 되어야 하기 때문 
SELECT pl.id, pl.name, pl.host_id
FROM places AS pl
RIGHT JOIN hv_hst_id AS hv 
ON pl.host_id = hv.host_id 
ORDER BY id;
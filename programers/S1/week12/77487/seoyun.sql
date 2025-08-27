-- 1. 헤비유저 id 찾아서 필터링
-- 2. 그 id 정보 찾아서 출력


WITH heavy_user AS (
    SELECT host_id
    FROM places
    GROUP BY host_id
    HAVING COUNT(host_id) >= 2
)

SELECT places.id, places.name, places.host_id
FROM places JOIN heavy_user ON places.host_id=heavy_user.host_id
ORDER BY places.id;
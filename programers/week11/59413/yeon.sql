# 입양 시각 구하기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/59413

# R-CTE : 0~24시가 포함되는 테이블 구성
# cte(hour, count)
WITH RECURSIVE cte AS ( 
    SELECT 0 AS 'hour', 0 AS 'count'
    UNION ALL
    SELECT hour+1, count FROM cte WHERE hour < 23
), cte2 AS (
    SELECT HOUR(datetime) AS 'hour', COUNT(*) AS 'count'
    FROM animal_outs
    GROUP BY HOUR(datetime)
    ORDER BY hour
)

# cte : 0~23시까지의 시간과 0으로 초기화된 count를 가진 테이블
# cte2 : animal_outs 테이블에서 시간대별 count를 가진 테이블

SELECT a.hour, IFNULL(b.count, 0) AS count 
FROM cte AS a
LEFT JOIN cte2 AS b
ON a.hour=b.hour;
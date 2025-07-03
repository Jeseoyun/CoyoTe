-- 시간대별로 정렬
-- 시간 정보: animal_outs 테이블의 datetime 칼럼
-- datetime에서 시간만 뽑아내서 칼럼 만들기 -> groupby로 count 때리기

-- 없는 시간은 어떻게 0으로 만들지??
-- => gpt 선생님 힌트: RECURSIVE 써라 / 떠헉 재환쿤...

WITH RECURSIVE timetable AS (
    SELECT 0 as t

    UNION ALL

    SELECT t+1
    FROM timetable
    WHERE t < 23
)
SELECT timetable.t as hour, COUNT(animal_outs.datetime) as count
FROM timetable LEFT JOIN animal_outs
    on timetable.t = HOUR(animal_outs.datetime)
GROUP BY timetable.t
ORDER BY timetable.t;
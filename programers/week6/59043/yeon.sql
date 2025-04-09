# 있었는데요 없었습니다 

-- 풀이 설명: 
--     animal_ins 테이블과 animal_outs 테이블을 JOIN, 조건은 animal_id 
--     조인 후 조건으로 보호소에 들어온 날짜 (ins.datetime)가 입양된 날짜 (outs.datetime) 보다 큰 조건으로 필터링 
--     이후 보호소에 들어온 날짜를 기준으로 오름차순 정렬 

SELECT ins.animal_id, ins.name
FROM animal_ins AS ins
JOIN animal_outs AS outs 
ON ins.animal_id=outs.animal_id
WHERE outs.datetime < ins.datetime
ORDER BY ins.datetime ASC;
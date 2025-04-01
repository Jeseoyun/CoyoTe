-- 없어진 기록 찾기

-- # 입양 기록은 있지만, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회 

-- # + WHERE 절에 `ins.animal_name IS NULL` 을 조건으로 주는 경우 제대로 조회가 되지 않음
-- # -> animal_ins 테이블에 id 는 존재하지만 name 이 null 인 경우가 있음 (==보호소에 들어온 기록이 있지만 들어올 때 이름이 없는 경우?)

SELECT outs.animal_id, outs.name
FROM animal_outs AS outs
LEFT JOIN animal_ins AS ins ON outs.animal_id = ins.animal_id 
WHERE ins.animal_id IS NULL
-- # WHERE  ins.name IS NULL
ORDER BY outs.animal_id;
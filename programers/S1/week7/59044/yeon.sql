# 오랜 기간 보호한 동물(1)

SELECT ins.name, ins.datetime
FROM animal_ins AS ins 
LEFT JOIN animal_outs AS outs
ON ins.animal_id=outs.animal_id
WHERE outs.animal_id IS NULL
ORDER BY ins.datetime ASC
LIMIT 3;
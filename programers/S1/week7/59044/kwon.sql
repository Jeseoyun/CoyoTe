SELECT ins.name, ins.datetime
FROM animal_ins AS ins
WHERE ins.animal_id NOT IN (
    SELECT animal_id
    FROM animal_outs
)
ORDER BY ins.datetime
LIMIT 3
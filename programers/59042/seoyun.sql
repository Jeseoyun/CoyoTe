SELECT outs.animal_id AS ANIMAL_ID, outs.name AS NAME
FROM animal_outs AS outs
LEFT JOIN animal_ins AS ins
ON outs.animal_id=ins.animal_id
WHERE ins.animal_id IS NULL;
SELECT ins.animal_id, ins.animal_type, ins.name
FROM animal_ins AS ins
JOIN
animal_outs AS outs
ON ins.animal_id = outs.animal_id
WHERE ins.sex_upon_intake REGEXP 'Intact' 
    AND outs.sex_upon_outcome REGEXP 'Spayed|Neutered'
ORDER BY ins.animal_id
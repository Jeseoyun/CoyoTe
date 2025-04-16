SELECT ins.animal_id, ins.animal_type, ins.name
FROM animal_ins AS ins JOIN animal_outs AS outs
ON ins.animal_id=outs.animal_id
WHERE ins.sex_upon_intake
          LIKE "Intact %" and
    (outs.sex_upon_outcome="Spayed Female" OR outs.sex_upon_outcome="Neutered Male")
ORDER BY ins.animal_id;
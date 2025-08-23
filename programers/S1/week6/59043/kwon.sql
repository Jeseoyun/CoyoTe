SELECT a_in.animal_id, a_in.name
FROM animal_ins AS a_in
JOIN 
animal_outs AS a_out
ON a_in.animal_id = a_out.animal_id
where a_in.datetime > a_out.datetime
ORDER BY a_in.datetime
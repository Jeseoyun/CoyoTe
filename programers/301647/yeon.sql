SELECT ed.id, ed.genotype, ped.genotype AS parent_genotype
FROM ecoli_data AS ed
LEFT JOIN ecoli_data AS ped ON ed.parent_id = ped.id 
WHERE ed.genotype & ped.genotype = ped.genotype
ORDER BY ed.id 
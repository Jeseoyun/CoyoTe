SELECT
    A.ID,
    A.GENOTYPE,
    P.GENOTYPE AS PARENT_GENOTYPE 
FROM ECOLI_DATA AS A 
INNER JOIN ECOLI_DATA AS P ON A.PARENT_ID = P.ID
WHERE A.GENOTYPE & P.GENOTYPE = P.GENOTYPE
ORDER BY ID
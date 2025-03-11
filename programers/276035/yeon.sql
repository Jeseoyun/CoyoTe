# FrontEnd 개발자 찾기

SELECT DISTINCT(dev.id), dev.email, dev.first_name, dev.last_name
FROM developers AS dev 
JOIN skillcodes AS sc 
ON dev.skill_code & sc.code = sc.code 
WHERE sc.category = 'Front End'
ORDER BY dev.id ASC;

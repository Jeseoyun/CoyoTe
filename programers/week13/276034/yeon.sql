# 조건에 맞는 개발자 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/276034

# # 옛날 풀이 
# SELECT 
#     id, 
#     email,
#     first_name,
#     last_name 
# FROM 
#     developers 
# WHERE 1 = 1
#     AND (skill_code & (SELECT code FROM skillcodes WHERE name="Python") != 0
#         OR skill_code & (SELECT code FROM skillcodes WHERE name="C#") != 0)
# ORDER BY 
#     id ASC;

# 2025.06.11 풀이 
-- skillcodes 테이블에서 Python과 C#의 code를 가져와서
-- developers 테이블의 skill_code와 비교하여 조건에 맞는 개발자를 찾는다.
-- skill_code와 skillcodes의 code를 비트 연산자로 비교하여
-- 해당 기술을 보유한 개발자를 찾는다.
-- 조인 조건으로 dev.skill_code & sc.code != 0 을 사용하여 해당 스킬 코드가 있음을 확인하다.
SELECT id, email, first_name, last_name
FROM developers AS dev
LEFT JOIN skillcodes AS sc 
ON dev.skill_code & sc.code != 0  
WHERE sc.name IN ("Python", "C#")
ORDER BY id ASC;
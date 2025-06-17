-- 1. C#이랑 Python 코드 뽑아내기
-- 2. 조건: (C# or Python 코드) and (개발자 코드) 비트연산해서 1이면 -> 스킬 보유

WITH target_skill AS (
    SELECT code
    FROM skillcodes
    WHERE name IN ('Python', 'C#')
)

SELECT d.id, d.email, d.first_name, d.last_name
FROM developers AS d
WHERE EXISTS (
    SELECT d.id
    FROM target_skill
    WHERE d.skill_code & code > 0
)
ORDER BY d.id;
# 대장균들의 자식 수 구하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/299305

-- 풀이 설명
-- 1. 서브쿼리:  parent_id 별로 GROUP BY -> COUNT 를 사용하여 parent_id 별 자식 수를 가지는 서브 테이블 구성 
--     - parent_id 별로 자식 수를 카운팅 해서 가짐
--     - parent_id 가 없는 대장균의 (루트 대장균) 경우 NULL parent_id 가 NULL 
-- 2. LEFT JOIN: 메인 테이블 (ecoli_data) 와 LEFT JOIN 으로 결합. 이때, ON 조건은 메인 테이블의 id == 서브 테이블의 parent_id
--     - 즉, 메인 테이블의 컬럼을 기준으로 서브 테이블을 붙임 
--     - 이때, 서브 테이블에서 parent_id가 NULL인 레코드는 날아감
--     - 메인 테이블에서 서브 테이블의 parent_id 와 매칭되지 않는 레코드의 경우 child_count가 NULL 값을 가지게 됨 
-- 3. 메인쿼리: SELECT 절에서 메인 테이블 기준으로 id를 가져오고, 서브 테이블의 parent_id를 가져옴.
--     - parent_id 가 NULL인 경우 0 으로 채우도록 IFNULL 사용
-- 4. ORDER BY: id 기준으로 정렬 

SELECT ed.id, IFNULL(pd.child_count, 0) AS child_count
FROM ecoli_data AS ed 
LEFT JOIN (
    SELECT parent_id, COUNT(id) AS child_count
    FROM ecoli_data 
    GROUP BY parent_id
) AS pd
ON ed.id = pd.parent_id
ORDER BY ed.id;
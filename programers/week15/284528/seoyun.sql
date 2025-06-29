-- 1. 연도별로 평점 구하기(문제에는 조건이 없는데 반기별로 데이터가 존재해서 평균 내려야 하는듯)
-- 2. 평점에 따른 등급 및 성과금 비율 구하기
-- 3. 직원들별로 평점에 따라 성과금 구하기

WITH year_avg_grade AS (
    SELECT emp_no, AVG(score) as score
    FROM hr_grade
    WHERE year=2022
    GROUP BY emp_no
), bonus_info AS (
    SELECT
        emp_no, 
        CASE
            WHEN score >= 96 THEN 'S'
            WHEN score >= 90 THEN 'A'
            WHEN score >= 80 THEN 'B'
            ELSE 'C'
        END AS grade, 
        CASE
            WHEN score >= 96 THEN 0.2
            WHEN score >= 90 THEN 0.15
            WHEN score >= 80 THEN 0.1
            ELSE 0.0
        END AS bonus_ratio
    FROM year_avg_grade
)

SELECT e.emp_no, e.emp_name, b.grade, e.sal*b.bonus_ratio as bonus
FROM hr_employees as e
    JOIN bonus_info as b ON e.emp_no=b.emp_no
ORDER BY e.emp_no;
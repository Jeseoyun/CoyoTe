-- 사번, 성명, 평가 등급, 성과금
-- 부서 정보
-- 사원 정보
-- 사원 평가 정보
WITH avg_emp AS (
    SELECT he.emp_no, he.emp_name, he.sal,
        CASE
            WHEN AVG(hg.score) >= 96 THEN 'S'
            WHEN AVG(hg.score) >= 90 THEN 'A'
            WHEN AVG(hg.score) >= 80 THEN 'B'
            ELSE 'C'
    END AS grade
    FROM hr_employees AS he
        LEFT JOIN
        hr_grade AS hg
        ON he.emp_no = hg.emp_no
    GROUP BY he.emp_no
)

SELECT emp_no, emp_name, grade,
    CASE
        WHEN grade = 'S' THEN sal * 0.2
        WHEN grade = 'A' THEN sal * 0.15
        WHEN grade = 'B' THEN sal * 0.1
        WHEN grade = 'C' THEN 0
        ELSE NULL
    END AS bonus
FROM avg_emp
ORDER BY emp_no
# 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/284528


# 기준 점수에 따른 평가 등급 CTE 
# 사원 번호로 group by 해서 score 의 평균울 각각의 기준 점수에 맞추어 분기 
WITH grades AS (
    SELECT emp_no,
        CASE 
            WHEN AVG(score) >= 96 THEN "S"
            WHEN AVG(score) >= 90 THEN "A"
            WHEN AVG(score) >= 80 THEN "B"
            ELSE "C"
        END AS grade 
    FROM hr_grade 
    GROUP BY emp_no
)


# hr_employees 테이블과 grades CTE를 left join (emp_no) -> 모든 사원이 조회되어야 하므로 left join 
# grade 에 따라 연봉에 정해진 비율을 곱하여 성과금을 계산 
# 사원 번호를 기준으로 오름차순 
SELECT emp.emp_no, emp.emp_name, grd.grade, 
    CASE 
        WHEN grd.grade = "S" THEN sal * 0.2 
        WHEN grd.grade = "A" THEN sal * 0.15 
        WHEN grd.grade = "B" THEN sal * 0.1
        ELSE 0 
    END AS bonus 
FROM hr_employees AS emp
LEFT JOIN grades AS grd
ON emp.emp_no = grd.emp_no 
ORDER BY emp.emp_no ASC;
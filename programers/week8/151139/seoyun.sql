-- 1. 서브쿼리에서 8~10월에 대여횟수가 5회 이상인 차 필터링
-- 2. 원래 테이블과 JOIN
-- 3. 월별, id별로 다시 GROUP BY
-- 4. 정렬

SELECT MONTH(history.start_date) AS month, history.car_id, COUNT(*) AS records
FROM car_rental_company_rental_history AS history
    JOIN (
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE YEAR(start_date)=2022 AND MONTH(start_date) BETWEEN 8 AND 10
        GROUP BY car_id
        HAVING COUNT(*) >= 5
    ) AS filtered
    ON history.car_id = filtered.car_id
WHERE YEAR(history.start_date)=2022 AND MONTH(history.start_date) BETWEEN 8 AND 10
GROUP BY MONTH(history.start_date), history.car_id
ORDER BY month ASC, history.car_id DESC;
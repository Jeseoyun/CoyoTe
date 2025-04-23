# 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

SELECT MONTH(start_date) AS month, car_id, COUNT(*) AS records
FROM car_rental_company_rental_history 
WHERE car_id
IN(
    SELECT DISTINCT(car_id)
    FROM car_rental_company_rental_history
    WHERE start_date BETWEEN "2022-08-01" AND "2022-11-01"
    GROUP BY car_id
    HAVING COUNT(*) >= 5
    ORDER BY car_id
)
AND MONTH(start_date) BETWEEN 8 AND 10
GROUP BY  car_id, month
ORDER BY month ASC, car_id DESC;
# 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/157339

# 세단과 SUV의 30일 할인률 from discount_plan
WITH discount_rate_month AS (
    SELECT car_type, discount_rate
    FROM car_rental_company_discount_plan
    WHERE car_type in ("세단", "SUV")
        AND duration_type LIKE "30%"
),
# 11월 예약 불가능한 차 
# WHERE 조건이 중요! 
able_in_nov AS (
    SELECT DISTINCT(car_id)
    FROM car_rental_company_rental_history 
    WHERE end_date >= '2022-11-01' AND start_date <= '2022-11-30'
    ORDER BY car_id
)

SELECT car.car_id, car.car_type, 
    ROUND(car.daily_fee * 30 * ((100 - discount_rate)*0.01)) AS FEE
FROM car_rental_company_car AS car 
JOIN discount_rate_month AS discount
ON car.car_type = discount.car_type
WHERE car.car_id NOT IN (SELECT * FROM able_in_nov) 
    AND car.car_type in ("세단", "SUV") 
HAVING fee >= 500000 AND fee < 2000000
ORDER BY fee DESC, car_type ASC, car_id DESC;


# WHERE 절의 subquery 대신 JOIN 을 사용하려고 시도했으나 내 머리로는 해결이 되지 않음. 
# GEMINI 사용해서 해결해 달라 함.

-- 30일 할인율이 적용되는 세단과 SUV
WITH discount_rate_month AS (
    SELECT car_type, discount_rate
    FROM car_rental_company_discount_plan
    WHERE car_type IN ('세단', 'SUV')
      AND duration_type LIKE '30%'
),
-- 11월에 대여 기록이 있는 자동차
rented_in_nov AS (
    SELECT DISTINCT car_id
    FROM car_rental_company_rental_history
    WHERE end_date >= '2022-11-01' AND start_date <= '2022-11-30'
)

SELECT
    c.car_id,
    c.car_type,
    ROUND(c.daily_fee * 30 * (100 - d.discount_rate) / 100) AS FEE
FROM
    car_rental_company_car AS c
-- 11월에 대여 기록이 있는 차와 LEFT JOIN
LEFT JOIN
    rented_in_nov AS r ON c.car_id = r.car_id
-- 할인율 정보를 가져오기 위한 INNER JOIN
JOIN
    discount_rate_month AS d ON c.car_type = d.car_type
WHERE
    -- JOIN 결과가 NULL인 경우(11월 대여 기록이 없는 차)만 필터링
    r.car_id IS NULL
HAVING
    FEE >= 500000 AND FEE < 2000000
ORDER BY
    FEE DESC,
    c.car_type ASC,
    c.car_id DESC;

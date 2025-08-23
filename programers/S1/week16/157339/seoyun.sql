-- 1. 원하는 차종이면서 기간 내에 대여가 가능한 자동차를 필터링한다
-- 시작일이 2022-11-30 이전이고 종료일이 2022-11-01 이후이면 대여 중이므로 빌릴 수 없다. 걔들은 제거하고 행 뽑아낸다.
-- 2. 30일 이상 대여 시 할인율을 적용해서 대여 30일 금액을 구하고 조건에 맞게 필터링

WITH possible_filtered_car AS (
    SELECT car_id, car_type, daily_fee
    FROM car_rental_company_car AS car
    WHERE car_type IN ('세단', 'SUV') AND NOT EXISTS (
        SELECT 1
        FROM car_rental_company_rental_history AS hist
        WHERE hist.car_id=car.car_id AND hist.start_date <= '2022-11-30' AND hist.end_date >= '2022-11-01'
      )
)
SELECT fc.car_id, fc.car_type, ROUND(fc.daily_fee*30*(100-dp.discount_rate)*0.01, 0) AS fee
FROM possible_filtered_car AS fc
JOIN car_rental_company_discount_plan AS dp ON dp.car_type=fc.car_type AND dp.duration_type='30일 이상'
WHERE ROUND(fc.daily_fee*30*(100-dp.discount_rate)*0.01, 0) >= 500000 AND ROUND(fc.daily_fee*30*(100-dp.discount_rate)*0.01, 0) < 2000000
ORDER BY FEE DESC, car_type, car_id DESC;
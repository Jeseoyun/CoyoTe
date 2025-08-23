-- 1. 통풍시트, 열선시트, 가죽시트 중 하나 이상이 포함된 자동차 고르고
-- 2. 종류별로 묶어서 몇 대인지 출력

WITH option_car AS (
    SELECT car_id, car_type
    FROM car_rental_company_car
    WHERE (options LIKE "%통풍시트%") OR (options LIKE "%열선시트%") OR (options LIKE "%가죽시트%")
)

SELECT car_type, COUNT(*) AS cars
FROM option_car
GROUP BY car_type
ORDER BY car_type;
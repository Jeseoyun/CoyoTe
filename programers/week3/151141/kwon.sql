-- # -- 코드를 입력하세요
-- # SELECT *
-- # FROM (SELECT car_id, daily_fee
-- #      FROM car_rental_company_car
-- #      WHERE car_type = '트럭') AS truck
-- #      JOIN
-- #      (SELECT history_id, car_id, (end_date - start_date) AS duration
-- #      FROM car_rental_company_rental_history) AS history
-- #      ON truck.car_id = history.car_id
-- #      JOIN
-- #      (SELECT duration_type, discount_rate
-- #      FROM car_rental_company_discount_plan
-- #      WHERE car_type = '트럭') AS truck_discount
-- #      ON
-- #         CASE
-- #             WHEN history.duration >= 7 THEN (SELECT discount_rate
-- #                                              FROM truck_discount
-- #                                              WHERE duration_type = '7일 이상')
-- #             WHEN history.duration >= 30 THEN (SELECT discount_rate
-- #                                              FROM truck_discount
-- #                                              WHERE duration_type = '30일 이상')
-- #             WHEN history.duration >= 90 THEN (SELECT discount_rate
-- #                                              FROM truck_discount
-- #                                              WHERE duration_type = '90일 이상')
-- #             ELSE 0

WITH value AS (
    SELECT car.daily_fee, car.car_type, his.history_id,
           DATEDIFF(end_date, start_date) + 1 AS period,
    CASE 
      WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
      ELSE 'NONE' END AS duration_type
FROM car_rental_company_rental_history AS his
INNER JOIN car_rental_company_car AS car ON car.car_id = his.car_id
WHERE car.car_type = '트럭')   



SELECT value.history_id, 
    ROUND(value.daily_fee * value.period * 
          (100 - IFNULL(plan.discount_rate,0)) / 100) AS FEE
FROM value
LEFT JOIN car_rental_company_discount_plan AS plan 
    ON plan.duration_type = value.duration_type 
    AND plan.car_type = value.car_type
ORDER BY 2 DESC, 1 DESC

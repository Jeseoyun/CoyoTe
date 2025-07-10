WITH cars_with_fee AS (
    SELECT
        c.car_id,
        c.car_type,
        FLOOR(c.daily_fee * 30 * (100 - p.discount_rate) / 100) AS fee
    FROM
        car_rental_company_car AS c
    JOIN
        car_rental_company_discount_plan AS p ON c.car_type = p.car_type
    WHERE
        c.car_type IN ('세단', 'SUV')
        AND p.duration_type = '30일 이상'
)
SELECT
    car_id,
    car_type,
    fee
FROM
    cars_with_fee
WHERE
    car_id NOT IN (
        SELECT
            car_id
        FROM
            car_rental_company_rental_history
        WHERE
            end_date >= '2022-11-01' AND start_date <= '2022-11-30'
    )
    AND fee >= 500000 AND fee < 2000000
ORDER BY
    fee DESC,
    car_type ASC,
    car_id DESC;
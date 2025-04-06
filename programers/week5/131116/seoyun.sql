SELECT mp.category, mp.max_price, f.product_name
FROM food_product AS f
    JOIN
        (SELECT category, MAX(price) AS max_price
        FROM food_product
        WHERE category IN ('과자', '국', '김치', '식용유')
        GROUP BY category
        ) AS mp
    ON f.category=mp.category and f.price=mp.max_price
ORDER BY max_price DESC;



-- SELECT category, MAX(price) AS max_price, product_name
-- FROM food_product
-- WHERE category IN ('과자', '국', '김치', '식용유')
-- GROUP BY category
-- ORDER BY max_price DESC;
--
-- select category, price
-- from food_product
SELECT food_product.category, food_product.price AS max_price, food_product.product_name
FROM food_product, (
    SELECT category, MAX(price) AS max_price
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category
) AS max_price_product
WHERE food_product.category = max_price_product.category AND food_product.price = max_price_product.max_price
ORDER BY price DESC


# SELECT category, MAX(price)
#     FROM food_product
#     WHERE category IN ('과자', '국', '김치', '식용유')
#     GROUP BY category
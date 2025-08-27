    SELECT DATE_FORMAT(sales_date,"%Y-%m-%d") AS sales_date, product_id, user_id, sales_amount
    FROM online_sale
    WHERE MONTH(sales_date) = 3
UNION
    SELECT DATE_FORMAT(sales_date,"%Y-%m-%d") AS sales_date, product_id, NULL AS user_id, sales_amount
    FROM offline_sale
    WHERE MONTH(sales_date) = 3
ORDER BY sales_date, product_id, user_id
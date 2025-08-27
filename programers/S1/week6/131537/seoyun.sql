-- 코드를 입력하세요
SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, user_id, sales_amount
FROM online_sale
WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-03'
UNION ALL
SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, NULL AS user_id, sales_amount
FROM offline_sale
WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-03'
ORDER BY sales_date, product_id, user_id;

-- SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, user_id, sales_amount
-- FROM online_sale
-- UNION ALL
-- SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, NULL AS user_id, sales_amount
-- FROM offline_sale
-- WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-03'
-- ORDER BY sales_date, product_id, user_id;
-- 상품 별 오프라인 매출 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131533


# CTE: product_id 별 오프라인 매출량 
WITH offline_sales_summation AS (
    SELECT product_id, SUM(sales_amount) AS sales_amount
    FROM offline_sale
    GROUP BY product_id
    ORDER BY product_id
)

SELECT product_code, (p.price * oss.sales_amount) AS sales 
FROM product AS p
JOIN offline_sales_summation AS oss 
ON p.product_id = oss.product_id 
ORDER BY sales DESC, product_code ASC;



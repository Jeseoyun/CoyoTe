-- 상품 코드 별 매출액 구하기
-- 상품 코드 기준으로 table join해서 매출액(판매량*가격) 계산

SELECT product_code, SUM(sales_amount*price) AS sales
FROM product
    JOIN offline_sale ON product.product_id=offline_sale.product_id
GROUP BY product_code
ORDER BY sales DESC, product_code;
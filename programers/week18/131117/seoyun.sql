WITH filtered AS (
    SELECT product_id, amount
    FROM food_order
    WHERE YEAR(produce_date)=2022 AND MONTH(produce_date)=5
)
SELECT p.product_id, p.product_name, p.price*SUM(f.amount) AS total_sales
FROM food_product AS p JOIN filtered AS f ON p.product_id=f.product_id
GROUP BY product_id
ORDER BY total_sales DESC, product_id;
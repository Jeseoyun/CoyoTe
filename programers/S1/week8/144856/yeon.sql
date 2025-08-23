# 저자 별 카테고리 별 매출액 집계하기

# 세 테이블을 모두 INNER JOIN 해서 책-저자-판매 통합 CTE 구성 
WITH cte AS (
    SELECT b.book_id, b.category, b.price, a.author_id, a.author_name, bs.sales_date, bs.sales
    FROM book AS b
    INNER JOIN author AS a
    ON b.author_id = a.author_id 
    INNER JOIN book_sales AS bs 
    ON b.book_id = bs.book_id 
)
# SELECT * FROM cte;
SELECT author_id, author_name, category, SUM(price * sales) AS total_sales 
FROM cte 
WHERE sales_date LIKE "2022-01%"
GROUP BY author_id, category 
ORDER BY author_id ASC, category DESC;
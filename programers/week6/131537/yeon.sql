# 오프라인/온라인 판매 데이터 통합하기

-- # 재미있는 사실: Programmers의 offline_sales 테이블에는 2022년 3월 판매 데이터가 존재하지 않는다. 
-- SELECT *
-- FROM offline_sale
-- WHERE sales_date BETWEEN '2022-03-01' AND '2022-03-31';

-- 풀이 설명: 
--     전처리 (날짜 필터링, user_id NULL 처리 (offline_sale 한정)) 를 한 CTE를 각각 정의 
--     두 개의 CTE를 UNION ALL 로 행 방향 concat
--     sales_date 의 형식을 "%Y-%m-%d" 로 수정 (문제 조건)
--     판매일, 상품 ID, 유저 ID를 기준으로 정렬


WITH processed_offline_sale AS (
    SELECT sales_date, product_id, NULL AS user_id, sales_amount
    FROM offline_sale
    WHERE sales_date BETWEEN '2022-03-01' AND '2022-03-31'
),
processed_online_sale AS (
    SELECT sales_date, product_id, user_id, sales_amount
    FROM online_sale
    WHERE sales_date BETWEEN '2022-03-01' AND '2022-03-31'
)

SELECT DATE_FORMAT(sales_date, "%Y-%m-%d") AS sales_date, product_id, user_id, sales_amount
FROM processed_offline_sale
UNION ALL
SELECT DATE_FORMAT(sales_date, "%Y-%m-%d") AS sales_date, product_id, user_id, sales_amount
FROM processed_online_sale
ORDER BY sales_date, product_id, user_id;

# 예전 풀이 (참고용)
select date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
from online_sale
where sales_date like "2022-03%"
union all
select date_format(sales_date, "%Y-%m-%d") as sales_date, product_id,
null as user_id, sales_amount
from offline_sale
where sales_date like "2022-03%"
order by sales_date asc, product_id asc, user_id asc;)
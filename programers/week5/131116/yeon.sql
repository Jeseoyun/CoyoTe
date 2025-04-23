# 식품분류별 가장 비싼 식품의 정보 조회하기 

-- CTE(Common Table Expression) 이용해서 과자, 국, 김치, 식용유 카테고리별 가장 비싼 가격을 가지는 max_price 구성
-- 기존 food_product 테이블과 JOIN (RIGHT JOIN ㅆㄱㄴ), 이때 조건(ON)은 food_product의 category 컬럼과 max_price의 category가 동일해야하며,
-- 동시에 food_product의 price 컬럼 값과 max_price의 max_price 컬럼 값이 동일해야 한다. 
-- 그래야지, 어떤 상품이 최대 가격을 갖는지 알 수 있음.

WITH max_price AS (
    SELECT category, MAX(price) AS max_price 
    FROM food_product
    WHERE category regexp "과자|국|김치|식용유"
    GROUP BY category
)

SELECT fp.category, mp.max_price, fp.product_name
FROM food_product AS fp 
JOIN max_price as mp 
ON fp.category = mp.category AND fp.price = mp.max_price
ORDER BY mp.max_price DESC;

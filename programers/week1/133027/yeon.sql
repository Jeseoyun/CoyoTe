# 주문량이 많은 아이스크림들 조회하기

SELECT fh.flavor
FROM first_half as fh 
INNER JOIN (
    SELECT flavor, SUM(total_order) AS total_order
    FROM july 
    GROUP BY flavor
) AS jul
ON fh.flavor = jul.flavor
ORDER BY (fh.total_order + jul.total_order) DESC
LIMIT 3;
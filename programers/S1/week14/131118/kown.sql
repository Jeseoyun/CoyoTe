-- 코드를 입력하세요
WITH rm AS (SELECT ri.rest_id,
            ri.rest_name,
            ri.food_type,
            ri.favorites,
            ri.address,
            ROUND(AVG(review_score), 2) AS score
    FROM rest_info AS ri
        JOIN
        rest_review AS rr
        ON ri.rest_id = rr.rest_id
    WHERE ri.address LIKE "서울%"
    GROUP BY ri.rest_id, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS)

SELECT *
FROM rm
ORDER BY score DESC, favorites DESC;
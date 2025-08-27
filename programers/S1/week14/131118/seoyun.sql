WITH avg_score AS (
    SELECT rest_id, ROUND(AVG(review_score), 2) AS score
    FROM rest_review
    GROUP BY rest_id
)

SELECT info.rest_id, info.rest_name, info.food_type, info.favorites, info.address, avg_score.score
FROM rest_info AS info
    JOIN avg_score ON info.rest_id=avg_score.rest_id
WHERE info.address LIKE '서울%'
ORDER BY avg_score.score DESC, info.favorites DESC;
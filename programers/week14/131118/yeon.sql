# 서울에 위치한 식당 목록 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/131118

# CTE: 서울에 위치한 식당 리스트 
WITH seoul_rest AS (
    SELECT *
    FROM rest_info
    WHERE address LIKE "서울%"
),
# CTE: 식당 평균 리뷰 점수 
avg_reviews AS (
    SELECT rest_id, ROUND(AVG(review_score), 2) AS score
    FROM rest_review
    GROUP BY rest_id
)

# 최종 쿼리: 서울에 위치한 식당 목록과 평균 리뷰 점수 출력
# LEFT JOIN 으로 두 CTE를 결합하는 경우 식당 리뷰가 없는 식당들도 쿼리 결과에 포함되는데, 이는 오답으로 처리 됨. 
# 따라서 INNER JOIN 으로 결합하여 리뷰가 있는 식당만 출력
SELECT seoul_rest.rest_id, seoul_rest.rest_name, seoul_rest.food_type, seoul_rest.favorites,
seoul_rest.address, avg_reviews.score 
FROM seoul_rest AS seoul_rest
JOIN avg_reviews AS avg_reviews 
ON seoul_rest.rest_id = avg_reviews.rest_id
ORDER BY score DESC, favorites DESC;
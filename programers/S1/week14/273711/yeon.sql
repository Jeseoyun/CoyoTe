# 업그레이드 된 아이템 구하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/273711

# CTE: rare items
WITH rare_item AS (
    SELECT item_id
    FROM item_info 
    WHERE rarity = "RARE"
)

# item_info 와 item_tree 테이블을 LEFT JOIN 
# rare_item 테이블과 item_tree 테이블을 JOIN (inner join)
# LEFT JOIN 하는 경우 업그레이드 전 아이템의 희귀도가 RARE가 아닌 경우도 포함되므로 INNER JOIN 사용 
SELECT info.item_id, info.item_name, info.rarity
FROM item_info AS info 
LEFT JOIN item_tree AS tree 
ON info.item_id = tree.item_id 
JOIN rare_item AS rare 
ON tree.parent_item_id = rare.item_id 
ORDER BY item_id DESC;
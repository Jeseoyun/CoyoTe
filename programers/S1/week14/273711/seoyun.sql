-- 1. 먼저 상위(parent) 아이템을 찾아서 매칭시켜준다
-- 2. 상위 아이템의 정보를 가져와서 보여준다

SELECT p_info.item_id, p_info.item_name, p_info.rarity
FROM item_info AS info
    JOIN item_tree AS parent ON info.item_id=parent.parent_item_id
    JOIN item_info AS p_info ON parent.item_id=p_info.item_id
WHERE info.rarity='RARE'
ORDER BY p_info.item_id DESC;
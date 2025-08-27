# 업그레이드 할 수 없는 아이템 구하기

SELECT info.item_id, info.item_name, info.rarity
FROM item_info AS info
WHERE info.item_id NOT IN (SELECT DISTINCT(parent_item_id) FROM item_tree WHERE parent_item_id IS NOT NULL)
ORDER BY item_id DESC;
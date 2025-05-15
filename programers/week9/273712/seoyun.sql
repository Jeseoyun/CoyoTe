-- 부모 트리에 자식 트리를 붙인다
-- 자식이 없으면(null) 업그레이드 불가능
WITH no_upgrade AS (
    SELECT p.item_id as item_id
    FROM item_tree AS p
        LEFT JOIN item_tree AS c
        ON p.item_id=c.parent_item_id
    WHERE c.item_id IS NULL
)

SELECT item_info.item_id, item_name, rarity
FROM item_info JOIN no_upgrade
    ON item_info.item_id=no_upgrade.item_id
ORDER BY item_info.item_id DESC;

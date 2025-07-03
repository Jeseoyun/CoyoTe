WITH null_item as (SELECT t1.item_id
    FROM item_tree as t1
        LEFT JOIN
        item_tree as t2
        ON t1.item_id = t2.parent_item_id
    WHERE t2.item_id IS NULL
)

SELECT ii.item_id, ii.item_name, ii.rarity
FROM null_item as ni
    JOIN
    item_info as ii
    ON ni.item_id = ii.item_id
ORDER BY ii.item_id DESC
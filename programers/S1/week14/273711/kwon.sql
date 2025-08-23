WITH rare_item AS (
    SELECT it.item_id
    FROM item_info AS ii
        JOIN
        item_tree AS it
        ON ii.item_id = it.parent_item_id
    WHERE rarity = "RARE"
)

# SELECT *
# FROM rare_item

SELECT ii.item_id, ii.item_name, ii.rarity
FROM rare_item AS ri
    JOIN
    item_info AS ii
    ON ri.item_id = ii.item_id
ORDER BY ii.item_id DESC

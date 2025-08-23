WITH highest_views AS (
    SELECT board_id
    FROM used_goods_board
    ORDER BY views DESC
    LIMIT 1
)

SELECT CONCAT('/home/grep/src/', ugf.board_id, '/', file_id, file_name, file_ext) AS file_path
FROM used_goods_file AS ugf
    JOIN highest_views as hv ON ugf.board_id=hv.board_id
ORDER BY file_id DESC;

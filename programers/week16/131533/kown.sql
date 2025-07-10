SELECT pd.product_code, SUM(os.sales_amount) * pd.price as sales
FROM product as pd
    JOIN
    offline_sale as os
    ON pd.product_id = os.product_id
GROUP BY pd.product_id
ORDER BY sales DESC, pd.product_code ASC
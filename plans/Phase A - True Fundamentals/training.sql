CTE refacrtored

#Finds the category_id with HAVING of at least 3 products and provides the product_id for the items in those categories. Deduple CTE
WITH eligible_product AS 
    (SELECT product_id
    FROM products
    WHERE category_id IN(                      
        SELECT category_id
        FROM products
        GROUP BY category_id
        HAVING COUNT(*) >= 3)),

#Filters the products by the product_id of the items in the categories with at least 3 products.
#This CTE will be used to join with the order_items table to get the relevant order items for those products.

eligible_order_items AS (
    SELECT order_id,
            product_id,
            quantity,
            unit_price
    FROM order_items
    WHERE product_id IN(
            SELECT product_id
            FROM eligible_product)),

# Filter the customers that are from the USA. 
usa_customers AS (
    SELECT customer_id,
           customer_name
    FROM customers
    WHERE country = 'USA'
),

# This CTE calculates the total amount spent by each customer in the USA on completed orders in 2025 for products in categories with at least 3 products. 
# It joins the orders table with th CTE to get the relevant order items and sums up the total spent for each customer.
customer_totals AS(
        SELECT orders.customer_id,
                 SUM(eligible_order_items.quantity * eligible_order_items.unit_price) AS total_spent
          FROM orders 
          JOIN eligible_order_items
          ON orders.order_id = eligible_order_items.order_id

          WHERE orders.status = 'completed'
            AND orders.order_date >= '2025-01-01'
            AND orders.order_date < '2026-01-01'
            AND orders.customer_id IN (
                SELECT customer_id 
                FROM usa_customers)

          GROUP BY orders.customer_id),

# This CTE filters the customers to only include those whose total spent is above the average total spent of all customers in the customer_totals CTE.
customer_avg AS(
    SELECT customer_id
      FROM customer_totals
      
      WHERE total_spent > (SELECT AVG(total_spent) FROM customer_totals)
              ),

# The final SELECT statement retrieves the customer_id, customer_name, and total_spent for customers who are from the USA 
# and have spent more than the average total spent on products in categories with at least 3 products in 2025.
SELECT customers.customer_id,
       customers.customer_name,
       customer_totals.total_spent
FROM customers
JOIN customer_totals
ON customers.customer_id = customer_totals.customer_id
WHERE customer_id IN (SELECT customer_id FROM customer_avg);

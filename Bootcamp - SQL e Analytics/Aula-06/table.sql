SELECT product_id,
    sum((((quantity)::double precision * unit_price) * ((1)::double precision - discount))) AS sold_value,
    rank() OVER (ORDER BY (sum((((quantity)::double precision * unit_price) * ((1)::double precision - discount)))) DESC) AS rank
   FROM order_details det
  GROUP BY product_id
-- Classificação dos produtos mais venvidos  usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- FROM order_details o JOIN products p ON p.product_id = o.product_id;

-- relatório apresenta o ID de cada pedido juntamente com o total de vendas e a classificação percentual e a distribuição cumulativa do valor de cada venda em relação ao valor total das vendas para o mesmo pedido. Esses cálculos são realizados com base no preço unitário e na quantidade de produtos vendidos em cada pedido. usando PERCENT_RANK() e CUME_DIST()
-- FROM order_details;

-- Listar funcionários dividindo-os em 3 grupos usando NTILE
-- FROM employees;

-- Ordenando os custos de envio pagos pelos clientes de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
-- FROM orders JOIN shippers ON shippers.shipper_id = orders.ship_via;

-- Faça a classificação dos produtos mais venvidos usando usando RANK(), DENSE_RANK() e ROW_NUMBER()
-- Essa questão tem 2 implementações, veja uma que utiliza subquery e uma que não utiliza.
-- Tabelas utilizadasFROM order_details o JOIN products p ON p.product_id = o.product_id;

-- Listar funcionários dividindo-os em 3 grupos usando NTILE
-- FROM employees;

-- Ordenando os custos de envio pagos pelos clientes de acordo 
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
-- FROM orders JOIN shippers ON shippers.shipper_id = orders.ship_via;

-- Desafio extra: questão intrevista Google
-- https://medium.com/@aggarwalakshima/interview-question-asked-by-google-and-difference-among-row-number-rank-and-dense-rank-4ca08f888486#:~:text=ROW_NUMBER()%20always%20provides%20unique,a%20continuous%20sequence%20of%20ranks.
-- https://platform.stratascratch.com/coding/10351-activity-rank?code_type=3
-- https://www.youtube.com/watch?v=db-qdlp8u3o
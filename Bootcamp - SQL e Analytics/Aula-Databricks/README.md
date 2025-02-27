Comandos para zerar as tabelas

```python
%python
dbutils.fs.rm("dbfs:/user/hive/warehouse/", True)
```

```sql
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customer_customer_demo;
DROP TABLE IF EXISTS customer_demographics;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employee_territories;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS order_details;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS region;
DROP TABLE IF EXISTS shippers;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS territories;
DROP TABLE IF EXISTS transacoes_clientes;
DROP TABLE IF EXISTS us_states;
```
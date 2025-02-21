%sql
-- Aula de SQL para a Sabesp: Criação de Tabelas no Databricks

-- Introdução
-- Nesta aula, dedicada à equipe da Sabesp, vamos explorar os conceitos fundamentais de SQL com foco na criação de tabelas no Databricks. Abordaremos a estrutura básica das tabelas, os tipos de dados disponíveis e as melhores práticas para organizar informações de forma eficiente utilizando o formato Delta Lake. Ao final, você terá um script consolidado para criar múltiplas tabelas de forma otimizada.

-- Script Completo para Criação de Tabelas no Databricks com Delta Lake

-- categories
CREATE TABLE categories (
    category_id SMALLINT NOT NULL,
    category_name STRING NOT NULL,
    description STRING,
    picture BINARY
) USING DELTA;

-- customer_customer_demo
CREATE TABLE customer_customer_demo (
    customer_id STRING NOT NULL,
    customer_type_id STRING NOT NULL
) USING DELTA;

-- customer_demographics
CREATE TABLE customer_demographics (
    customer_type_id STRING NOT NULL,
    customer_desc STRING
) USING DELTA;

-- customers
CREATE TABLE customers (
    customer_id STRING NOT NULL,
    company_name STRING NOT NULL,
    contact_name STRING,
    contact_title STRING,
    address STRING,
    city STRING,
    region STRING,
    postal_code STRING,
    country STRING,
    phone STRING,
    fax STRING
) USING DELTA;

-- employees
CREATE TABLE employees (
    employee_id SMALLINT NOT NULL,
    last_name STRING NOT NULL,
    first_name STRING NOT NULL,
    title STRING,
    title_of_courtesy STRING,
    birth_date DATE,
    hire_date DATE,
    address STRING,
    city STRING,
    region STRING,
    postal_code STRING,
    country STRING,
    home_phone STRING,
    extension STRING,
    photo BINARY,
    notes STRING,
    reports_to SMALLINT,
    photo_path STRING
) USING DELTA;

-- employee_territories
CREATE TABLE employee_territories (
    employee_id SMALLINT NOT NULL,
    territory_id STRING NOT NULL
 ) USING DELTA;

-- order_details
CREATE TABLE order_details (
    order_id SMALLINT NOT NULL,
    product_id SMALLINT NOT NULL,
    unit_price FLOAT NOT NULL,
    quantity SMALLINT NOT NULL,
    discount FLOAT NOT NULL
) USING DELTA;

-- orders
CREATE TABLE orders (
    order_id SMALLINT NOT NULL,
    customer_id STRING,
    employee_id SMALLINT,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    ship_via SMALLINT,
    freight FLOAT,
    ship_name STRING,
    ship_address STRING,
    ship_city STRING,
    ship_region STRING,
    ship_postal_code STRING,
    ship_country STRING
) USING DELTA;

-- products
CREATE TABLE products (
    product_id SMALLINT NOT NULL,
    product_name STRING NOT NULL,
    supplier_id SMALLINT,
    category_id SMALLINT,
    quantity_per_unit STRING,
    unit_price FLOAT,
    units_in_stock SMALLINT,
    units_on_order SMALLINT,
    reorder_level SMALLINT,
    discontinued INT NOT NULL
) USING DELTA;

-- region
CREATE TABLE region (
    region_id SMALLINT NOT NULL,
    region_description STRING NOT NULL
) USING DELTA;

-- shippers
CREATE TABLE shippers (
    shipper_id SMALLINT NOT NULL,
    company_name STRING NOT NULL,
    phone STRING
) USING DELTA;

-- suppliers
CREATE TABLE suppliers (
    supplier_id SMALLINT NOT NULL,
    company_name STRING NOT NULL,
    contact_name STRING,
    contact_title STRING,
    address STRING,
    city STRING,
    region STRING,
    postal_code STRING,
    country STRING,
    phone STRING,
    fax STRING,
    homepage STRING
) USING DELTA;

-- territories
CREATE TABLE territories (
    territory_id STRING NOT NULL,
    territory_description STRING NOT NULL,
    region_id SMALLINT NOT NULL
) USING DELTA;

-- us_states
CREATE TABLE us_states (
    state_id SMALLINT NOT NULL,
    state_name STRING,
    state_abbr STRING,
    state_region STRING
) USING DELTA;

-- Fim do script

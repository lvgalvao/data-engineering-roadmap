# Aula 12 : Database Indexing

Vamos detalhar cada parte do código:

1. **Criação da Tabela:**
   - Exemplo:
     ```sql
     CREATE TABLE pessoas (
         id SERIAL PRIMARY KEY,
         first_name VARCHAR(3),
         last_name VARCHAR(3),
         estado VARCHAR(3)
     );
     ```

2. **Inserção de 1 Milhão de Registros:**

   ```sql
   CREATE OR REPLACE FUNCTION random_estado()
   RETURNS VARCHAR(3) AS $$
   BEGIN
      RETURN CASE floor(random() * 5)
            WHEN 0 THEN 'SP'
            WHEN 1 THEN 'RJ'
            WHEN 2 THEN 'MG'
            WHEN 3 THEN 'ES'
            ELSE 'DF'
            END;
   END;
   $$ LANGUAGE plpgsql;

   -- Inserir dados na tabela pessoas com estados aleatórios
   INSERT INTO pessoas (first_name, last_name, estado)
   SELECT 
      substring(md5(random()::text), 0, 3),
      substring(md5(random()::text), 0, 3),
      random_estado()
   FROM 
      generate_series(1, 10000000);
     ```

3. **Criando um INDEX no first_name**

```sql
CREATE INDEX first_name_index ON pessoas(first_name)
```

4. **Fazendo  uma busca usando um INDEX**

```sql
SELECT COUNT(*) FROM pessoas WHERE first_name = 'aa'
```

Total query runtime: 585 msec.

5. **Fazendo  uma busca sem usar INDEX**

```sql
SELECT COUNT(*) FROM pessoas WHERE last_name = 'aa'
```

Total query runtime: 2 secs 552 msec.

6. **Vamos criar uma tabela com particionamento**


```sql
     CREATE TABLE pessoas (
         id SERIAL PRIMARY KEY,
         first_name VARCHAR(3),
         last_name VARCHAR(3),
         estado VARCHAR(3)
     ) PARTITION BY RANGE (id);
```

Opção mais simples

```sql
CREATE TABLE pessoas_part1 PARTITION OF pessoas FOR VALUES FROM (MINVALUE) TO (2000001);
CREATE TABLE pessoas_part2 PARTITION OF pessoas FOR VALUES FROM (2000001) TO (4000001);
CREATE TABLE pessoas_part3 PARTITION OF pessoas FOR VALUES FROM (4000001) TO (6000001);
CREATE TABLE pessoas_part4 PARTITION OF pessoas FOR VALUES FROM (6000001) TO (8000001);
CREATE TABLE pessoas_part5 PARTITION OF pessoas FOR VALUES FROM (8000001) TO (MAXVALUE);
```

Opção indireta

```sql
-- Criar as tabelas particionadas
CREATE TABLE pessoas_part1 (
    LIKE pessoas INCLUDING ALL,
    CHECK (id >= 1 AND id <= 2000000)
);

CREATE TABLE pessoas_part2 (
    LIKE pessoas INCLUDING ALL,
    CHECK (id > 2000000 AND id <= 4000000)
);

CREATE TABLE pessoas_part3 (
    LIKE pessoas INCLUDING ALL,
    CHECK (id > 4000000 AND id <= 6000000)
);

CREATE TABLE pessoas_part4 (
    LIKE pessoas INCLUDING ALL,
    CHECK (id > 6000000 AND id <= 8000000)
);

CREATE TABLE pessoas_part5 (
    LIKE pessoas INCLUDING ALL,
    CHECK (id > 8000000)  -- A última partição não precisa de limite superior
);
```

```sql
ALTER TABLE pessoas ATTACH PARTITION pessoas_part1 FOR VALUES FROM (MINVALUE) TO (2000001);
ALTER TABLE pessoas ATTACH PARTITION pessoas_part2 FOR VALUES FROM (2000001) TO (4000001);
ALTER TABLE pessoas ATTACH PARTITION pessoas_part3 FOR VALUES FROM (4000001) TO (6000001);
ALTER TABLE pessoas ATTACH PARTITION pessoas_part4 FOR VALUES FROM (6000001) TO (8000001);
ALTER TABLE pessoas ATTACH PARTITION pessoas_part5 FOR VALUES FROM (8000001) TO (MAXVALUE);
```

```sql
   INSERT INTO pessoas (first_name, last_name, estado)
   SELECT 
      substring(md5(random()::text), 0, 3),
      substring(md5(random()::text), 0, 3),
      random_estado()
   FROM 
      generate_series(1, 10000000);
```

## Funciona

```sql
select * from pessoas
```


## Criando com base em lista

```sql
CREATE TABLE pessoas (
    id SERIAL,
    first_name VARCHAR(3),
    last_name VARCHAR(3),
    estado VARCHAR(3),
    PRIMARY KEY (id, estado)
) PARTITION BY LIST (estado);

-- Criar as partições
CREATE TABLE pessoas_sp PARTITION OF pessoas FOR VALUES IN ('SP');
CREATE TABLE pessoas_rj PARTITION OF pessoas FOR VALUES IN ('RJ');
CREATE TABLE pessoas_mg PARTITION OF pessoas FOR VALUES IN ('MG');
CREATE TABLE pessoas_es PARTITION OF pessoas FOR VALUES IN ('ES');
CREATE TABLE pessoas_df PARTITION OF pessoas FOR VALUES IN ('DF');
```
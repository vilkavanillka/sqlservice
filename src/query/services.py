create_products_tables = """
CREATE TABLE product_category (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);
CREATE TABLE product (
  id INT PRIMARY KEY,
  category_id INT,
  name VARCHAR(100)
);"""

insert_products_tables = """

INSERT INTO product_category VALUES (1, 'Food');
INSERT INTO product_category VALUES (2, 'Gadget');

INSERT INTO product VALUES (1, 1, 'Milk');
INSERT INTO product VALUES (2, 1, 'Pineapples');
INSERT INTO product VALUES (3, 2, 'Apple iPhone 15');"""

select_products_tables = """"""
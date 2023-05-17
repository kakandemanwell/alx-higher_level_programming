-- script  creates a table second_table in the database hbtn_0c_0 in a MySQL server and add multiples rows.

DROP TABLE IF EXISTS second_table;
CREATE TABLE second_table (id INTEGER, name VARCHAR(256), score INTEGER);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);

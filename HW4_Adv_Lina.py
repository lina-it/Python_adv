##Не совсем поняла нужно ли было в другом формате забрасывать сюда код или вот так:
##Если что, пиши. Спасибо!)

# CREATE TABLE orders(
# 	order_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
# 	created_dt date,
# 	updated_dt date,
# 	order_type text,
# 	description text,
# 	status text,
# 	serial_no integer,
# 	creator_id integer);
#
# CREATE TABLE employees(
# 	employee_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
# 	fio text,
# 	position_ text,
# 	department_id integer,
# 	foreign key(department_id) references departments(department_id)
# 	);
#
# CREATE TABLE departments(
# 	department_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
# 	department_name text);
##Не совсем поняла нужно ли было в другом формате забрасывать сюда код или вот так:
##Если что, пиши. Спасибо!)

"""CREATE TABLE if not exists departments(
	department_id serial PRIMARY KEY NOT NULL,
	department_name text);

CREATE TABLE if not exists employees(
	employee_id serial PRIMARY KEY NOT NULL,
	fio text,
	position text,
	department_id integer,
	foreign key(department_id) references departments(department_id)
	);

CREATE TABLE if not exists orders(
	order_id serial PRIMARY KEY NOT NULL,
	created_dt date,
	updated_dt date,
	order_type text,
	description text,
	status text,
	serial_no integer,
	creator_id integer,
	foreign key(creator_id) references employees(employee_id)
	);"""
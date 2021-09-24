# Создадим нашу базу данных, где будет храниться информация о департаментах, сотрудниках, заявках на ремонт оборудования
# и клиентах, обратившихся с проблемой.

import psycopg2
from sys import argv

print(argv)
DB_URL = 'postgresql://postgres:1111@127.0.0.1:5432/postgres'

CREATE_TABLE_QUERY = """CREATE TABLE if not exists departments(
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
	);

CREATE TABLE if not exists profiles(
    profile_id serial PRIMARY KEY NOT NULL,
    login text,
    password text,
    about_me text,
    is_subscribed bool,
    profile_tg_chat_id integer
	);"""

INSERT_QUERY_dep = """INSERT INTO departments (department_id, department_name) VALUES (%s,%s)"""
INSERT_QUERY_empl = """INSERT INTO employees (employee_id, fio, position, department_id) VALUES (%s,%s,%s,%s)"""
INSERT_QUERY_ord = """INSERT INTO orders (order_id, created_dt, updated_dt, order_type, description, status, serial_no, creator_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
INSERT_QUERY_prof = """INSERT INTO profiles (login, password, about_me, is_subscribed, profile_tg_chat_id) VALUES (%s,%s,%s,%s,%s)"""

data_dep = [
    ('1','IT'),
    ('2','Accounting'),
    ('3','Procurment'),
    ('4','Administration'),
    ('5','Finance')
]
data_empl = [
    ('1', 'TONY STARK', 'SOFTWARE ENGINEER', '1'),
    ('2', 'TIM ADOLF', 'SALESMAN', '3'),
    ('3', 'KIM JARVIS', 'MANAGER', '4'),
    ('4', 'SAM MILES', 'SALESMAN', '3'),
    ('5', 'KEVIN HILL', 'MANAGER', '4'),
    ('6', 'CONNIE SMITH', 'ANALYST', '1'),
    ('7', 'ALFRED KINSLEY', 'PRESIDENT', '4'),
    ('8', 'PAUL TIMOTHY', 'SALESMAN', '3'),
    ('9', 'JOHN ASGHAR', 'SOFTWARE ENGINEER', '1'),
    ('10', 'ROSE SUMMERS', 'TECHNICAL LEAD', '1'),
    ('11', 'ANDREW FAULKNER', 'ANAYLYST', '1'),
    ('12', 'KAREN MATTHEWS', 'SOFTWARE ENGINEER', '1'),
    ('13', 'TIM ADOLF', 'ACCOUNTANT', '2'),
    ('14', 'KIM JARVIS', 'ACCOUNTANT', '2'),
    ('15', 'SAM MILES', 'ACCOUNTANT', '2'),
    ('16', 'LINA DANILKOVYCH', 'FINANCE DIRECTOR', 5),
    ('17', 'OLHA VYDRYHAN', 'FINANCE CPECIALIST', 5)
]

data_ord = [
    (1, '01.08.21', '05.08.21', 1, 'first', 'approved', 56743, 2),
    (2, '01.08.21', '21.08.21', 2, 'second', 'approved', 67483, 2),
    (3, '01.08.21', '05.08.21', 1, 'third', 'opened', 56744, 2),
    (4, '01.08.21', '21.08.21', 2, 'another', 'opened', 67484, 4),
    (5, '01.08.21', '06.08.21', 1, 'other', 'canceled', 56745, 4),
    (6, '01.08.21', '22.08.21', 2, 'second', 'canceled', 67485, 4),
    (7, '01.08.21', '07.08.21', 1, 'first', 'approved', 56746, 2),
    (8, '01.08.21', '23.08.21', 2, 'second', 'approved', 67486, 2),
    (9, '01.08.21', '08.08.21', 1, 'third', 'opened', 56747, 4),
    (10, '01.08.21', '24.08.21', 2, 'another', 'opened', 67487, 4),
    (11, '01.08.21', '09.08.21', 1, 'other', 'canceled', 56748, 8),
    (12, '01.08.21', '25.08.21', 2, 'second', 'canceled', 67488, 2),
    (13, '01.08.21', '10.08.21', 1, 'first', 'approved', 56749, 4),
    (14, '01.08.21', '10.08.21', 2, 'second', 'approved', 67489, 2),
    (15, '01.08.21', '10.08.21', 1, 'third', 'opened', 56711, 8),
    (16, '01.08.21', '11.08.21', 2, 'another', 'opened', 67411, 8),
    (17, '01.08.21', '02.08.21', 1, 'other', 'canceled', 56722, 8),
    (18, '01.08.21', '31.08.21', 2, 'second', 'canceled', 67422, 2)
]

data_prof = [
    ('li', 'li01', 'something', False, 567432000),
    ('na', 'na01', 'information', False, 674832000),
    ('lina', 'li02', 'data-analyst', True, 334851700)
]



conn = psycopg2.connect(DB_URL)
with conn.cursor() as cursor:
    cursor.execute(CREATE_TABLE_QUERY)

    cursor.executemany(INSERT_QUERY_dep, data_dep)
    cursor.executemany(INSERT_QUERY_empl, data_empl)
    cursor.executemany(INSERT_QUERY_ord, data_ord)
    cursor.executemany(INSERT_QUERY_prof, data_prof)
    conn.commit()

# Необходимо реализовать следующий функционал:
# Управление данными:
# - Добавление, изменение, удаление информации о департаментах компании.
# - Добавление, изменение, удаление информации о сотрудниках компании.
# - Добавление, изменение, удаление информации о заявках на ремонт оборудования.
# - Добавление, изменение, удаление информации о клиентах, обратившихся с проблемой.

import psycopg2 as ps
import json
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, Response, redirect, url_for
from logging import getLogger
# from flask_script import Manager
from client import MyDbClient, MyTgClient

DB_URL = 'postgresql://postgres:1111@127.0.0.1:5432/postgres'
TOKEN = env.str("TOKEN")
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)
my_db_client = MyDbClient(DB_URL)
my_db_client.setup()

app.orders_db_client = my_db_client
logger = getLogger(__name__)

class departments(db.Model):
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(100))

    def __str__(self):
        return f"department_name: {self.department_name}"

class employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(100))
    position = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'))

    def __str__(self):
        return f"fio: {self.fio} | position: {self.position}"

class orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_dt = db.Column(db.Date)
    updated_dt = db.Column(db.Date)
    order_type = db.Column(db.String(15))
    description = db.Column(db.String(100))
    status = db.Column(db.String(15))
    serial_no = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))

    def __str__(self):
        return f"order_id: {self.order_id} | created_dt: {self.created_dt} | updated_dt: {self.updated_dt} | " \
               f"order_type: {self.order_type} | description: {self.description} |status: {self.status} | " \
               f"serial_no: {self.serial_no} | creator_id: {self.creator_id}"

class profiles(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100))
    about_me = db.Column(db.String(400))
    is_subscribed = db.Column(db.Boolean)
    profile_tg_chat_id = db.Column(db.Integer)

    def __str__(self):
        return f"login: {self.login} | about_me: {self.about_me} | is_subscribed: {self.is_subscribed}"


@app.route('/')
def time():
    return f"{dt.now()}"

@app.route("/get_orders")
def get_products():
    res = app.orders_db_client.get_orders(10)
    return Response(status=200, response=json.dumps(res))


class TokenError(Exception):
    def __str__(self):
        return "No token!"

    def __repr__(self):
        return "No token!"


TOKEN_LIST = [
    "11c786c0-0a03-4699-b838-b71fc931ceb5",
    "17e10009-c687-4729-ae13-04982e65bfe6"
]


def get_token_from_db(token):
    return token in TOKEN_LIST


def check_token(request_data):
    token = request_data.get("token")
    if not get_token_from_db(token):
        raise TokenError()


@app.route("/add_order", methods=["POST"])
def add_order():
    request_data = request.json
    try:
        check_token(request_data)
    except TokenError as err:
        return Response(status=403, response=str(err))
    order_data = request_data["order_info"]
    app.products_db_client.insert_new_product(order_type=order_data["order_type"],
                                              description=order_data["description"])
    return Response(status=200, response="OK")

@app.route("/check_method", methods=["GET", "POST", "UPDATE", "DELETE", "PUT"])
def check_method():
    return f"{request.method}"

@app.route('/create_employees_data', methods=["POST"])
def create_employees_data():
    for user_profile_data in zip(department, employees):
        department_id = Department(**user_profile_data[0]).save()
        Employees(department_id=department_id, **user_profile_data[1]).save()
    return "OK"

@app.route('/create_orders_data', methods=["POST"])
def create_orders_data():
    for orders_data in zip(employees, orders):
        creator_id = Employees(**orders_data[0]).save()
        Orders(creator_id=creator_id, **orders_data[1]).save()
    return "OK"

@app.route('/create_department', methods=["GET", "POST"])
def create_department():
    Department(created_dt=dt.now(), department_name='IT1').save()
    return "OK"


@app.route('/update_department')
def update_department():
    dep = Department.objects(department_name='IT16')
    dep.update(updated_dt=dt.now(), department_name='IT17')
    return "OK"


@app.route("/delete_department_data", methods=["GET", "DELETE"])
def delete_department_data():
    Department.objects.all().delete()
    return "OK"


@app.route('/department_by_id/<string:department_id>', methods=['GET', 'POST'])
def department_by_id(department_id):
    dep = Department.objects(id=department_id)
    return f"Result: {dep}"


@app.route('/create_employee', methods=["GET", "POST"])
def create_employee():
    Employees(created_dt=dt.now(), fio='Volodia', position='gamer').save()
    return "OK"

@app.route('/update_employees')
def update_employees():
    emp = Employees.objects(fio='Volodia', position='gamer' )
    emp.update(updated_dt=dt.now(), department_name='Zhenia', position='fytbotbolist')
    return "OK"


@app.route("/delete_employees_data", methods=["GET", "DELETE"])
def delete_employees_data():
    Employees.objects.all().delete()
    return "OK"


@app.route("/employee_by_fio/<string:fio>", methods=['GET'])
def employee_by_fio(fio):
    emp = Employees.objects(fio=fio)
    print(emp)
    return f"Result: {emp}"

@app.route('/create_orders', methods=["GET", "POST"])
def create_orders():
    Orders(created_dt=dt.now(), order_type='1', description='first', status='opened', serial_no='56777',
           creator_id='2').save()
    return "OK"


@app.route('/update_orders')
def update_orders():
    orde = Orders.objects(status='opened', serial_no='56743')
    orde.update(updated_dt=dt.now(), status='closed', serial_no='55555')
    return "OK"


@app.route("/delete_orders_data", methods=["GET", "DELETE"])
def delete_orders_data():
    Orders.objects.all().delete()
    return "OK"


@app.route("/orders_by_serial_no/<int:serial_no>", methods=['GET'])
def orders_by_serial_no(serial_no):
    orde = Orders.objects(serial_no=serial_no)
    print(orde)
    return f"Result: {orde}"


if __name__ == "__main__":
    app.run(debug=True)


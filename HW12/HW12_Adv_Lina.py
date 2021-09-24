# Начните писать своё собственное простое web-приложение.
# Можно использовать фреймворк Flask или Sanic (если решите писать асинхронное приложение) по вашему вкусу.
# Реализовать следующие endpoints ("ручки"):
#
# - создание заявки
# - изменение заявки
#
# В рамках выполнения задания вам потребуется взаимодействовать с БД Postgresql.
# Используйте для этого библиотеку psycopg2 или asyncpg (если решили писать асинхронный код).

import psycopg2 as ps
import json
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, Response, redirect, url_for
from logging import getLogger
# from flask_script import Manager

DB_URL = 'postgresql://postgres:1111@127.0.0.1:5432/postgres'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)

logger = getLogger(__name__)

class departments(db.Model):
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(100))

class employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(100))
    position = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'))

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


@app.route('/')
def time():
    return f"{dt.now()}"


@app.route("/check_method", methods=["GET", "POST", "UPDATE", "DELETE", "PUT"])
def check_method():
    return f"{request.method}"


@app.route('/create_orders_data', methods=["POST"])
def create_orders_data():
    for orders_data in zip(employees, orders):
        creator_id = Employees(**orders_data[0]).save()
        Orders(creator_id=creator_id, **orders_data[1]).save()
    return "OK"

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


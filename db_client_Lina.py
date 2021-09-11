import psycopg2

class DbClient:
    SELECT_QUERY1 = """SELECT * FROM orders where status= 'approved' and updated_dt= '21.08.21' and creator_id=2 limit 5"""
    SELECT_QUERY2 = """SELECT fio, department_name from employees e left join departments d on e.department_id =d.department_id limit 5"""
    SELECT_QUERY3 = """SELECT updated_dt, status, count(order_id) from orders group by status, updated_dt order by updated_dt limit 5"""
    SELECT_QUERY4 = """SELECT order_id, fio from orders o left join employees e on o.creator_id =e.employee_id limit 5"""

    def __init__(self, dsn):
        self.dsn = dsn
        self.connect = None
        db_pool = None

    def setup(self):
        self.connect = psycopg2.connect(self.dsn)

    def select_orders(self):
        with self.connect.cursor() as cursor:
           return cursor.fetch(self.SELECT_QUERY1)

    def close(self):
        self.connect.close()
        self.connect = None


class DbClientV2(DbClient):
    SELECT_QUERY1 = """SELECT * FROM orders where status= 'approved' and updated_dt= '21.08.21' and creator_id=2 
    limit 5 """

    def select_orders(self):
        with self.connect.cursor() as cursor:
            return cursor.fetch(self.SELECT_QUERY1)



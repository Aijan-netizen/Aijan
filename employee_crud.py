import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self, db_name="employee_db.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def insert(self, employee):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO employee (name, position, salary, hire_date)
                VALUES (?, ?, ?, ?)
            ''', (employee.name, employee.position, employee.salary, employee.hire_date))
            conn.commit()

    def get_by_id(self, id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))
            row = cursor.fetchone()
            return Employee(*row) if row else None

    def get_all(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employee')
            rows = cursor.fetchall()
            return [Employee(*row) for row in rows]

    def update(self, employee):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE employee
                SET name = ?, position = ?, salary = ?, hire_date = ?
                WHERE id = ?
            ''', (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
            conn.commit()

    def delete(self, id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM employee WHERE id = ?', (id,))
            conn.commit()

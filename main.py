from employee import Employee
from employee_dao import EmployeeDAO
from datetime import datetime

def main():
    dao = EmployeeDAO()

    # 1. Insert
    emp = Employee(name="Айжан", position="Тестировщик", salary=100000, hire_date=str(datetime.now().date()))
    dao.insert(emp)

    # 2. Get All
    print("Все сотрудники:")
    for e in dao.get_all():
        print(e)

    # 3. Get by ID
    print("\nСотрудник с ID = 1:")
    print(dao.get_by_id(1))

    # 4. Update
    emp_to_update = dao.get_by_id(1)
    if emp_to_update:
        emp_to_update.salary = 120000
        emp_to_update.name = "Айжан Обновлённая"
        dao.update(emp_to_update)

    # 5. Delete
    dao.delete(1)
    print("\nПосле удаления:")
    for e in dao.get_all():
        print(e)

if __name__ == "__main__":
    main()

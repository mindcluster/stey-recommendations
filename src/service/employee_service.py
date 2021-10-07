from src.config.database import DatabaseConnection


class EmployeeService:

    def __init__(self):
        self.model = ''
        self.db = DatabaseConnection()

    def get_best_employees(self):
        employees = self.db.get("SELECT * FROM EMPLOYEES;")

        best_employees = []

        for employee in employees:
            print(employee)
            best_employees.append({
                "id": employee['ID'],
                "name": employee['NOME'],
                "score": self.get_score(employee),
                "job": employee['JOB_TITLE']
            })

        return best_employees

    def get_score(self, employee):  # TODO: implement method
        return 96

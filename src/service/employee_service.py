import numpy as np
import pandas as pd

from src.config.database import DatabaseConnection
from src.service.employee_model import EmployeeModel


class EmployeeService:

    def __init__(self):
        self.model = ''
        self.db = DatabaseConnection()
        self.employeeModel = EmployeeModel()

    def get_all(self):
        employees = self.db.get("SELECT * FROM EMPLOYEES;")

        best_employees = []

        for employee in employees:
            best_employees.append({
                "id": employee['ID'],
                "name": employee['NOME'],
                "status": self.get_status(employee),
                "job": employee['JOB_TITLE']
            })

        return best_employees

    def get_by_id(self, id):
        employees = self.db.get(f"SELECT * FROM EMPLOYEES WHERE ID = {id};")

        for employee in employees:
            return {
                "id": employee['ID'],
                "name": employee['NOME'],
                "status": self.get_status(employee),
                "job": employee['JOB_TITLE']
            }

    def get_status(self, employee):  # TODO: implement method
        cols = ['EXP_LEV_ATUAL', 'PROPORCIONAL_HIRING_DATE', 'EXP_LEVEL_FUTURO', 'GENDER', 'SUB_SL']

        df_apt_test = pd.DataFrame(np.array([[employee['EXP_LEV_ATUAL'], employee['PROPORCIONAL_HIRING_DATE'],
                                              employee['EXP_LEVEL_FUTURO'], employee['GENDER'], employee['SUB_SL']]]),
                                   columns=cols)
        df_apt_test_cleaned = self.employeeModel.transform(df_apt_test)

        result = self.employeeModel.predict(df_apt_test_cleaned)

        return self.employeeModel.get_inverse_transform(result)

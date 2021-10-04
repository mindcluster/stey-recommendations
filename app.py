from flask import Flask
from src.service.employee_service import EmployeeService

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def best_employees():
    try:
        employee_service = EmployeeService()

        return {'status': 200,
                'data': employee_service.get_best_employees()}
    except Exception as e:
        return {'status': 500,
                'data': e}


if __name__ == '__main__':
    app.run()

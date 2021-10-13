import os

from flask import Flask

from src.service.employee_service import EmployeeService

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def get_employees():
    try:
        employee_service = EmployeeService()

        return {'status': 200,
                'data': employee_service.get_all()}
    except Exception as e:
        return {'status': 500,
                'data': e}


@app.route('/<id>', methods=['POST', 'GET'])
def get_employee_by_id(id):
    try:
        employee_service = EmployeeService()

        return {'status': 200,
                'data': employee_service.get_by_id(id)}
    except Exception as e:
        return {'status': 500,
                'data': e}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

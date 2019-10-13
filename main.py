import datetime
from application.people import get_employees
from application.salary import calculate_salary


def time():
    timenow = datetime.datetime.now()
    print(timenow)


if __name__ == '__main__':
    time()
    get_employees()
    calculate_salary()
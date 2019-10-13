from application.people import *
from application.salary import *
import datetime


def time():
    timenow = datetime.datetime.now()
    print(timenow)


if __name__ == '__main__':
    time()
    get_employees()
    calculate_salary()
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from art import text2art


def get_date():
    today = date.today()
    print(f'Сегодня {today}')

def design_it(text=str): 
   print(text2art(text, font='tarty1'))

if __name__ == '__main__':
    design_it("Hello world!")
    get_date()
    calculate_salary()
    get_employees()

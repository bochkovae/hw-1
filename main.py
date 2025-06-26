from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from datetime import datetime as dt
import requests

if __name__ == "__main__":
    print(dt.now().date())
    cs()
    ge()
    response = requests.get('https://google.com')
    print(response)
